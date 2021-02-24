from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "age", "gender"]
    list_filter = ["gender"]
    search_fields = ["username"]

