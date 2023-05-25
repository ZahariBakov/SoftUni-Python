from django.shortcuts import render, redirect

from car_collection_app.web.forms import ProfileForm, CarForm
from car_collection_app.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    else:
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def profile_details(request):
    return render(request, 'profile-details.html')


def profile_edit(request):
    return render(request, 'profile-edit.html')


def profile_delete(request):
    return render(request, 'profile-details.html')


def catalogue(request):
    cars = Car.objects.all()
    profile = Profile.objects.get()
    cars_count = cars.count()

    context = {
        'cars': cars,
        'profile': profile,
        'cars_count': cars_count
    }

    return render(request, 'catalogue.html', context)


def car_create(request):
    form = CarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    profile = Profile.objects.get()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'car-create.html', context)


def car_details(request, pk):
    return render(request, 'car-details.html')


def car_edit(request, pk):
    return render(request, 'car-edit.html')


def car_delete(request, pk):
    return render(request, 'car-delete.html')
