from django.urls import path, include

from online_library.main.views import index, add_book, book_details, profile_details, delete_profile, edit_profile, \
    edit_book

urlpatterns = (
    path('', index, name='index'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('details/<int:pk>', book_details, name='book details'),

    path('profile/', include([
        path('', profile_details, name='profile details'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
