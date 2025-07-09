from django.urls import path
from .views import CustomLoginView , CustomSignUpView , CustomLogOutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/' , CustomSignUpView.as_view() , name = 'signup'),
    path('' , CustomLoginView.as_view() , name='login'),
    path('logout/' , CustomLogOutView.as_view() , name='logout')
    
]