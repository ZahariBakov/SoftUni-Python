from django.urls import path
from django_introduction.tasks.views import show_bare_minimum_view, show_all_tasks, show_index

urlpatterns = (
    # http://localhost:8000/tasks/
    path('', show_index),
    # http://localhost:8000/tasks/it_works/
    path('it_works/', show_bare_minimum_view),
    # http://localhost:8000/tasks/all/
    path('all/', show_all_tasks),
)
