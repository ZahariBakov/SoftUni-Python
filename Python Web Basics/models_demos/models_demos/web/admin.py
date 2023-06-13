from django.contrib import admin

from models_demos.web.models import Employee, NullBlankDemo


# The `Employee` model is enabled in django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass
