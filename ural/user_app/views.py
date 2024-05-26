from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth import get_user_model
from django.contrib import messages
# from django.core.mail import send_mail
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_text
# from email.message import EmailMessage
from . tokens import generate_token
from ural import settings


def checkingNameEmail(request, email, name):
    if User.objects.filter(email=email):
        messages.error(request, 'Аккаунт для указанной электронной почты уже существует')
        return False
    
    if len(name) > 255:
        messages.error(request, 'Имя слишком длинное')
        return False
    
    if not name.isalnum():
        messages.error(request, 'Имя может состоять только из цифр и букв')
        return False
    return True

User = get_user_model()

def login(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            dj_login(request, user)
            return render(request, 'profile.html')
        else:
            messages.error(request, "Bad credentials")
            return render(request, 'index.html')

    return render(request, 'login.html')

def logout(request):
    dj_logout(request)
    messages.success(request, "Logged")
    return redirect('main:index')

def registration(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not checkingNameEmail(request, email, name):
            return redirect('user_app:registration')

        if password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('user_app:registration')

        user = User.objects.create_user(name=name, email=email, password=password1)
        
        # user.is_active = False
        user.save()
        messages.success(request, "Вы успешно зарегистрировались")

        # subject = 'Добро пожаловать на BSCAR-GO'
        # message = 'Добрый день,' + name + "\nВы зарегистрировались на BSCAR-GO\nСпасибо, что зашёл на наш сайте\nМы отправили тебе письмо с подтверждением твоей почты, пожалуйста подтверди свой адрес электронной почты, чтобы активировать свою учётную запись.\nСпасибо!\n"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [user.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        #Email address confirmation email
        # current_site = get_current_site(request)
        # email_subject = 'Проверьте вашу почту'
        # message2 = render_to_string('email_confirmation'), {
        #     'name': user.first.name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token': generate_token.make_token(user),
        # }

        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [user.email],
        # )

        # email.fail_silently = True
        # email.send()
        dj_login(request, user)
        return render(request, 'index.html')
        
    return render(request, 'registration.html')

def profile(request):
    print('profile')
    return render(request, 'profile.html')

def editProfile(request):
    print('edit')
    if request.POST:
        email = request.POST.get('email')
        name = request.POST.get('name')
        if not checkingNameEmail(request, email, name) and (email != request.user.email 
                                                            or name != request.user.name):
            return redirect('user_app:edit_profile')

        request.user.name = name
        request.user.email = email
        request.user.about_me = request.POST.get('aboutMe')
        request.user.save()
        print('edit')
        return redirect('user_app:profile')
    
    return render(request, 'editProfile.html')