from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('auth_demos.web.urls')),
]

# NEVER name auth app `auth`
# Name it `app_auth`, `my_auth`, `PROJECT_NAME_auth`

# auth - authentication or authorization

# Auth flow:
'''
# Authentication
The User sends credentials to a system
    - username $ password, phone number + sms code, authentication app

# Authorization
After authentication, the system authorizes the user
'''


'''
Web1 (web app)
    - SoftUni_key = '4124-4223-4123-543344-44445f'
Web2 (web app)
    - SoftUni_key = '4124-4223-4123-543344-44445f'
'''

'''
DB     ->  pbkdf2_sha256$600000$9M91RUowSVNHEIPcq1R7vk$Nfk9J8m4iKXwjGop0TfkZyUaad
12345  ->  pbkdf2_sha256$600000$9M91RUowSVNHEIPcq1R7vk$Nfk9J8m4iKXwjGop0TfkZyUaad
'''
