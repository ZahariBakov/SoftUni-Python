from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def profile_create(request):
    return render(request, 'profile-create.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def profile_edit(request):
    return render(request, 'profile-edit.html')


def profile_delete(request):
    return render(request, 'profile-details.html')


def catalogue(request):
    return render(request, 'catalogue.html')


def car_create(request):
    return render(request, 'car-create.html')


def car_details(request):
    return render(request, 'car-details.html')


def car_edit(request):
    return render(request, 'car-edit.html')


def car_delete(request):
    return render(request, 'car-delete.html')
