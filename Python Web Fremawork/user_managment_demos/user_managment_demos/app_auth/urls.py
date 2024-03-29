# app_auth/urls.py
from django.urls import path

from user_managment_demos.app_auth.views import RegisterUserView, LogoutUserView, LoginUserView, UsersListView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('', UsersListView.as_view(), name='users list'),
)


# Ba1kOv$!
