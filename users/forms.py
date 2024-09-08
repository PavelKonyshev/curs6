from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Класс форма для регистрации пользователей"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ManagerChangeUserForm(StyleFormMixin, ModelForm):
    """Форма для менеджера, который может заблокировать пользователя"""
    class Meta:
        model = User
        fields = ('is_active',)


class UserProfileChangeForm(StyleFormMixin, UserChangeForm):
    """Форма для редактирования профиля самим пользователем"""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        """Метод, чтобы скрыть из формы редактирования профиля поле с паролем"""
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()