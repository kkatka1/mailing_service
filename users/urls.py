from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users import views
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserListView
from users.views import UserCreateView


app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("user_list/", UserListView.as_view(), name="user_list"),
]
