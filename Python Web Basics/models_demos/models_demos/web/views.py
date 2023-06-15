from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from models_demos.web.models import Employee, Department


def index(request):
    # employees = Employee.objects.all()
    # `employees` is empty (unfulfilled) QuerySet
    # Less data from the DB is better
    employees = [e for e in Employee.objects.all() if e.department_id == 2] # Wong way to get data from DB

    # employees2 = Employee.objects.filter(department_id=2)\
    employees2 = Employee.objects\
        .filter(department__name='Engineering')\
        .order_by('last_name', 'first_name')
    # `department__name` in `filter` is like `department.name`

    # employees_list = list(employees)

    # print(list(User.objects.all()))
    # print(list(Department.objects.all()))
    # print(employees_list)
    # print(employees)

    # `get` returns an object, not QuerySet
    # `get` returns a single object and throws when none or multiple results
    # `get` is eager and does not return a QuerySet
    # print(Employee.objects.get(level=Employee.LEVEL_JUNIOR))

    get_object_or_404(Employee, level=Employee.LEVEL_REGULAR)

    Employee.objects.filter(level=Employee.LEVEL_SENIOR).first()

    department = Department.objects.get(pk=2)
    print(department)

    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'index.html', context)
