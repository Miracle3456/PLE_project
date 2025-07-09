from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView



class CustomLoginView(LoginView):
    success_url = 'home'
    template_name = 'accounts/login.html'

class CustomSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'accounts/signup.html'

class CustomLogOutView(LogoutView):
    success_url = 'login'