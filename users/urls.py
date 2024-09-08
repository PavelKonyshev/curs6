from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserListView, ManagerUserUpdateView, ProfileUpdateView, \
    ProfileDeleteView

app_name = UsersConfig.name

urlpatterns = [
    # Урлы для входа пользователя в систему, выхода из системы и регистрации, а так же редактирования профиля и его удаления
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile_delete/', ProfileDeleteView.as_view(), name='profile_delete'),


    # Урл для подтверждения почты
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),

    # Урлы для просмотра и редактирования пользователя модератором
    path('user/', UserListView.as_view(), name='user_list'),
    path('edit_user/<int:pk>/', ManagerUserUpdateView.as_view(), name='edit_user'),
]