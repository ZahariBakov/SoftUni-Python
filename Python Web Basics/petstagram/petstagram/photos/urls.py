from django.urls import path

from petstagram.photos.views import photo_details, edit_photo, delete_photo, \
    PhotoAddView

urlpatterns = [
    path('add/', PhotoAddView.as_view(), name='add photo'),
    path('<int:pk>/', photo_details, name='photo details'),
    path('edit/<int:pk>/', edit_photo, name='edit photo'),
    path('delete/<int:pk>/', delete_photo, name='delete photo'),
]
