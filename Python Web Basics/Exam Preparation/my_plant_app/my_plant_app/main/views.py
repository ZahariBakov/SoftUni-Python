from django.shortcuts import render, redirect

from my_plant_app.main.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from my_plant_app.main.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def index(request):
    context = {
        'plant': Plant.objects.all(),
        'profile': get_profile(),
    }

    return render(request, 'core/home-page.html', context)


def catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants,
        'profile': get_profile(),
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
        'profile': get_profile(),
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = get_profile()

    context = {
        'profile': profile,
        'plants': Plant.objects.all(),
        'plant_count': Plant.objects.all().count(),
    }

    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)

    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)


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
        'profile': get_profile(),
    }

    return render(request, 'plant/create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant,
        'profile': get_profile(),
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
        'profile': get_profile(),
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
        'profile': get_profile(),
    }

    return render(request, 'plant/delete-plant.html', context)
