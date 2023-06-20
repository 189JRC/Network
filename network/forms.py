from django import forms
from .models import Profile, User


class UserEditForm(forms.ModelForm):
    # direct CP from book
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
