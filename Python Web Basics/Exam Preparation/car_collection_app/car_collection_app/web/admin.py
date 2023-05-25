from django.contrib import admin

from car_collection_app.web.models import Profile, Car


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    pass
