from django.contrib.auth.models import User
from django.shortcuts import render

from models_demos.web.models import Employee, Department


def index(request):
    x = list(Employee.objects.all())
    print(list(User.objects.all()))
    print(list(Department.objects.all()))
    print(x)

