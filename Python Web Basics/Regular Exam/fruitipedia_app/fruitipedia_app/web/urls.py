from django.urls import path, include

from fruitipedia_app.web.views import index, dashboard, fruit_create, fruit_details, edit_fruit, delete_fruit, \
    profile_create, profile_details, edit_profile, delete_profile

urlpatterns = (
    path('', index, name='index'),

    path('dashboard/', dashboard, name='dashboard'),

    path('create/', fruit_create, name='fruit create'),
    path('<int:pk>/', include([
        path('details/', fruit_details, name='fruit details'),
        path('edit/', edit_fruit, name='edit fruit'),
        path('delete/', delete_fruit, name='delete fruit'),
    ])),

    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
