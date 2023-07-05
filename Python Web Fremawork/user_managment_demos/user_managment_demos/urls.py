from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_managment_demos.web.urls')),
    path('auth/', include('user_managment_demos.app_auth.urls')),
]
