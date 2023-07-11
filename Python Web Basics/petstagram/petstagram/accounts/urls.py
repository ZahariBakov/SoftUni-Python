from django.urls import path, include

from petstagram.accounts.views import RegisterUserView, delete_profile, edit_profile, show_profile_details, \
    LoginUserView, LogoutUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', show_profile_details, name='profile details'),
        path('edit/', edit_profile, name='profile edit'),
        path('delete/', delete_profile, name='profile delete'),
    ])),
]
