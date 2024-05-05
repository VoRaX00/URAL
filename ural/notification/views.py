from django.shortcuts import render

# Create your views here.
def allNotification(request):
    return render(request, 'notification.html')