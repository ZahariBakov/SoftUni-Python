from django.urls import path
from departments_app.departments.views import sample_view

urlpatterns = [
    path('', sample_view),
    path('<departemnt_id>/', sample_view),
]
