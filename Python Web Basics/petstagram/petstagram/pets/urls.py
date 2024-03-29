from django.urls import path, include
from petstagram.pets.views import add_pet, pet_details, edit_pet, delete_pet

urlpatterns = [
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', pet_details, name='pet details'),
        path('edit/', edit_pet, name='edit pet'),
        path('delete/', delete_pet, name='delete pet'),
    ])),
]
