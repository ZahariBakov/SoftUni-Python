from django.shortcuts import render
from django import http


# Create your views here.
def show_bare_minimum_view(request):
    return http.HttpResponse('It works')
