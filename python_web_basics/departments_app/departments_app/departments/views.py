from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_departments(request, *args, **kwargs):
    body = f'path=: {request.path}, args={args}, kwargs={kwargs}'

    return HttpResponse(body)

