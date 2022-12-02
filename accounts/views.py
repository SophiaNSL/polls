from django.shortcuts import render
from accounts.models import User

# Create your views here.

def user_info(request):

    user = User.objects.get(pk=1)
    return render(request,'accounts/user_info.html', {
        'user':user
    })