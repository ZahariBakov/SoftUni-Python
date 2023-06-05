from django.urls import path

from game_play_app.web.views import index, dashboard, create_profile, details_profile, edit_profile, delete_profile, \
    create_game, details_game, edit_game, delete_game

urlpatterns = [
    path('', index, name='index'),

    path('dashboard/', dashboard, name='dashboard'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('game/create/', create_game, name='create game'),
    path('game/details/<int:pk>/', details_game, name='details game'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/delete/<int:pk>/', delete_game, name='delete game'),
]
