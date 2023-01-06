from django.urls import path
from django_introduction.tasks.views import show_bare_minimum_view

urlpatterns = (
    path('', show_bare_minimum_view),
)
