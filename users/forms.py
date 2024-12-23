from django.contrib.auth.forms import UserCreationForm
from django import forms
from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserManagerForm(forms.ModelForm):
    class Meta:
        model = User
        # Указываем поля, которые можно редактировать
        fields = ['email', 'phone', 'country', 'avatar']


class UserChangePasswordForm(forms.Form):
    need_generate = forms.BooleanField()
    email = forms.EmailField(required=True)
