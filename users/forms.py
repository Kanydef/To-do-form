from django  import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(label="день рождения",
        widget=forms.DateInput(attrs={"type":"date", "class":"form-class"}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age", "gender","birthday")
