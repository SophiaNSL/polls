from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('user/info/', views.user_info, name='user_info'),
   

]