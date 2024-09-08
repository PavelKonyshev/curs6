import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from users.forms import UserRegisterForm, ManagerChangeUserForm, UserProfileChangeForm
from users.models import User

# Импортирую почту
from dotenv import load_dotenv
import os
load_dotenv()

# Create your views here.
class UserCreateView(CreateView):
    """Класс контроллер для регистрации пользователей"""
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Метод для того, чтобы поставить пользователю статус неактивный, сгенерировать ему токен и отправить на почту"""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтвердите свою электронную почту',
            message=f'Здравствуйте, перейдите по ссылке для подтверждения вашей почты {url}',
            from_email=os.getenv('mail'),
            recipient_list=[user.email],
        )
        return super().form_valid(form)

def email_verification(request, token):
    """Метод для подтверждения почты пользователя"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserListView(ListView):
    """Класс-контроллер для вывода всех пользователей"""
    model = User


class ManagerUserUpdateView(UpdateView):
    """Класс контролер для редактирования пользователей модератором"""
    model = User
    form_class = ManagerChangeUserForm
    success_url = reverse_lazy('users:user_list')
    template_name = 'users/manager_change_profile.html'


class ProfileUpdateView(UpdateView):
    """Класс-контроллер для редактирования профиля сами пользователем"""
    model = User
    form_class = UserProfileChangeForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """Метод для получения пользователя, чтобы понять какого пользователя мы редактируем"""
        return self.request.user


class ProfileDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:login')
    template_name = 'users/profile_delete.html'


    def get_object(self, queryset=None):
        """Метод для получения пользователя, чтобы понять какого пользователя мы редактируем"""
        return self.request.user