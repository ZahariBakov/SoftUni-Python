from django.urls import path, include

from petstagram.accounts.views import RegisterUserView, LoginUserView, LogoutUserView, \
    ProfileEditView, ProfileDeleteView, ProfileDetailsView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
    ])),
]
