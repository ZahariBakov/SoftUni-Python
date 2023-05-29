from django.urls import path

from my_plant_app.main.views import index, catalogue, profile_create, profile_details, profile_edit, profile_delete, \
    plant_create, plant_details, plant_edit, plant_delete

urlpatterns = (
    path('', index, name='index'),

    path('catalogue/', catalogue, name='catalogue'),

    path('profile/create/', profile_create, name='profile create'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),

    path('create/', plant_create, name='plant create'),
    path('details/<plant_id>/', plant_details, name='plant details'),
    path('edit/<plant_id>/', plant_edit, name='plant edit'),
    path('delete/<plant_id>/', plant_delete, name='plant delete'),
)
