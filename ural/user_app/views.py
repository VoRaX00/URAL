from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

# Create your views here.
def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user=user)
    return render(request, 'login.html')

def logout(request):
    pass

def registration(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        user = User.objects.create_user(name, email, password1)
        user.save()
        messages.success(request, "Вы успешно зарегистрировались")

        return redirect('main:index')
        
    return render(request, 'registration.html')

def profile(request):
    print(request.user)
    return render(request, 'profile.html')


# class Register(View):
#     template_name = 'registration.html'

#     def get(self, request):
#         context = {
#             'form': UserCreationForm()
#         }
#         return render(request, self.template_name, context)
    
#     def post(self, request):
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=password)
#             login(user)
#             return redirect('main:index')
        
#         context = {
#             'form': form
#         }

#         return render(request, self.template_name, context)