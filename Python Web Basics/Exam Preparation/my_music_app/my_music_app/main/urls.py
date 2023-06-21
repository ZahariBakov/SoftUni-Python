from django.urls import path, include

from my_music_app.main.views import index, album_detail, edit_album, delete_album, profile_details, delete_profile, \
    add_album

urlpatterns = (
    path('', index, name='index'),

    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', album_detail, name='album details'),
        path('<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),

    path('profile/', include([
        path('details/', profile_details, name='profile details'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
