from django.shortcuts import render, redirect

from my_plant_app.main.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm
from my_plant_app.main.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def index(request):
    profile = get_profile()

    if profile is None:
        return render(request, 'core/home-page.html')

    context = {
        'plant': Plant.objects.all(),
        'hide_nav': True,
    }

    return render(request, 'core/home-page.html', context)


def catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
    }
    return render(request, 'core/catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_edit(request):
    return render(request, 'profile/edit-profile.html')


def profile_delete(request):
    return render(request, 'profile/delete-profile.html')


def plant_create(request):
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'hide_nav': True,
    }

    return render(request, 'plant/create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant,
    }

    return render(request, 'plant/plant-details.html', context)


def plant_edit(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'plant/edit-plant.html', context)


def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'plant/delete-plant.html', context)
