from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    pass

class CustomPasswordResetForm(PasswordResetForm):
    pass

class CustomSetPasswordForm(SetPasswordForm):
    pass 