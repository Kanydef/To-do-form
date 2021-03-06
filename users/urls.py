from django.urls import path
from .views import UserList, UserCreate

urlpatterns = [
    path("", UserList.as_view(), name="users_list"),
    path("create/", UserCreate.as_view(), name="users_create"),
]