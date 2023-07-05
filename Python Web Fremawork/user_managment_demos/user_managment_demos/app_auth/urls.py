# app_auth/urls.py
from django.urls import path

from user_managment_demos.app_auth.views import RegisterUserView, LogoutUserView, LoginUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
)


# Ba1kOv$!
