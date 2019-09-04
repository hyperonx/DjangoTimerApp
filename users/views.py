from django.urls import reverse_lazy
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class PasswordResetView(TemplateView):
    template_name = 'registration/password_reset_form.html'
