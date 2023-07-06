from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_managment_demos.web.urls')),
    path('auth/', include('user_managment_demos.app_auth.urls')),
]


def hash_example(value):
    return value % 7

# hash_example(8) -> 1
# hash_example(6) -> 6
# hash_example(13) -> 6
