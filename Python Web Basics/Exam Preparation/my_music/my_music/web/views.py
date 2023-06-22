from django.shortcuts import render, redirect

from my_music.web.forms import CreateProfileForm
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
    pass


def album_details(request):
    pass


def edit_album(request):
    pass


def delete_album(request):
    pass


def profile_details(request):
    pass


def delete_profile(request):
    pass
