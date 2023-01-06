from django.urls import path
from django_introduction.tasks.views import index

urlpatterns = (
    path('', index),
)
