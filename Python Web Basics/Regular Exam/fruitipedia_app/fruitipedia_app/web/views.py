from django.shortcuts import render, redirect

from fruitipedia_app.web.forms import CreatProfileForm, CreateFruitForm, EditFruitForm, DeleteFruitForm, EditProfileForm
from fruitipedia_app.web.models import Profile, Fruit


def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }

    return render(request, 'core/index.html', context)


def dashboard(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'core/dashboard.html', context)


def fruit_create(request):
    profile = Profile.objects.first()

    form = CreateFruitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'fruit': fruit,
    }

    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.filter(pk=pk).get()

    form = EditFruitForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.filter(pk=pk).get()
    form = DeleteFruitForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruit/delete-fruit.html', context)


def profile_create(request):
    form = CreatProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    posts = Fruit.objects.count()

    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }

    return  render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()

    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index')

    return render(request, 'profile/delete-profile.html')

