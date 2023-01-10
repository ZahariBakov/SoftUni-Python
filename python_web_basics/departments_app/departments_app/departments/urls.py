from django.urls import path
from departments_app.departments.views import show_departments

urlpatterns = [
    # /departments/
    path('', show_departments),

    # /departments/{id}/
    path('<departemnt_id>/', show_departments),

    # /departments/int/{id}/
    path('int/<int:department_id>/', show_departments),
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
