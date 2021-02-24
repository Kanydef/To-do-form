from django.shortcuts import render
from .models import CustomUser
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class UserList(ListView):
    model= CustomUser
    template_name = "user/users_list.html"

class UserCreate(CreateView):
    model = CustomUser
    template_name = "user/users_create.html"
    form_class = CustomUserCreationForm
    # fields = ("username","age","gender","password")
    success_url = reverse_lazy("users_list")