from django.shortcuts import render, redirect

from game_play_app.web.forms import ProfileCreateForm
from game_play_app.web.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.first()
    except:
        return None


def index(request):
    context = {
        'profile': get_profile,
    }
    return render(request, 'core/home-page.html', context)


def dashboard(request):
    context = {
        'profile': get_profile,
        'games': Game.objects.all(),
    }

    return render(request, 'core/dashboard.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    return render(request, 'profile/details-profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')


def create_game(request):
    return render(request, 'game/create-game.html')


def details_game(request, pk):
    return render(request, 'game/details-game.html')


def edit_game(request, pk):
    return render(request, 'game/edit-game.html')


def delete_game(request, pk):
    return render(request, 'game/delete-game.html')
