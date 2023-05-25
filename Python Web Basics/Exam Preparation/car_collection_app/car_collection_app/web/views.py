from django.shortcuts import render, redirect

from car_collection_app.web.forms import ProfileForm, CarForm, EditCarForm, DeleteCarForm, EditProfileForm
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
    profile = get_profile()
    cars = Car.objects.all()
    total_cars_price = sum(c.price for c in cars)

    context = {
        'profile': profile,
        'total_cars_price': total_cars_price,
    }

    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile details')

    form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    cars = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        cars.delete()

        return redirect('index')

    context = {
        'profile': profile,
    }

    return render(request, 'profile-delete.html', context)


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
    car = Car.objects.get(pk=pk)

    context = {
        'car': car,
        'profile': Profile.objects.get(),
    }
    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    form = EditCarForm(instance=car)

    context = {
        'form': form,
        'profile': Profile.objects.first(),
        'car': car,
    }

    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)

    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': get_profile(),
        'car': car,
    }

    return render(request, 'car-delete.html', context)
