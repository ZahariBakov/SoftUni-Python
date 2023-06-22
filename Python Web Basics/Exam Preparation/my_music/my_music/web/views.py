from django.shortcuts import render, redirect

from my_music.web.forms import CreateProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm
from my_music.web.models import Album
from my_music.web.templatetags.get_profile import get_user_profile


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()

    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'core/home-no-profile.html', context)


def index(request):
    profile = get_user_profile()

    if not profile:
        return redirect('create profile')

    context = {
        'albums': Album.objects.all()
    }

    return render(request, 'core/home-with-profile.html', context)


def add_album(request):
    form = AddAlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album,
    }

    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    form = EditAlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    form = DeleteAlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/delete-album.html', context)


def profile_details(request):
    profile = get_user_profile()
    albums_count = Album.objects.all().count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    profile = get_user_profile()
    albums = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('index')

    return render(request, 'profile/profile-delete.html')
