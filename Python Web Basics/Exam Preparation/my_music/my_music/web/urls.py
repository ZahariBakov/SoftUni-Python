from django.urls import path, include

from my_music.web.views import index, add_album, album_details, edit_album, delete_album, profile_details, \
    delete_profile, create_profile

urlpatterns = (
    path('', index, name='index'),

    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', album_details, name='album details'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),

    path('profile/', include([
        path('add/', create_profile, name='create profile'),
        path('details/', profile_details, name='profile details'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)

