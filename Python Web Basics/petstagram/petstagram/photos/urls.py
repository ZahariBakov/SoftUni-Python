from django.urls import path

from petstagram.photos.views import add_photo, photo_details, edit_photo, delete_photo

urlpatterns = [
    path('add/', add_photo, name='add photo'),
    path('<int:pk>/', photo_details, name='photo details'),
    path('edit/<int:pk>/', edit_photo, name='edit photo'),
    path('delete/<int:pk>/', delete_photo, name='delete photo'),
]
