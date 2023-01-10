from django.urls import path
from departments_app.departments.views import sample_view

urlpatterns = [
    # /departments/
    path('', sample_view),

    # /departments/{id}/
    path('<departemnt_id>/', sample_view),

    # /departments/int/{id}/
    path('int/<int:department_id>/', sample_view),
]

# paths = (
#     '',
#     '<department_id>/',
#     'int/<int:department_id>/',
# )
#
# urlpatterns = [path(url, sample_view) for url in paths]


# urlpatterns = ()
# urlpatterns += (path('', sample_view),)
# urlpatterns += (path('<department_id>/', sample_view),)
# urlpatterns += (path('int/<int:department_id>/', sample_view),)
