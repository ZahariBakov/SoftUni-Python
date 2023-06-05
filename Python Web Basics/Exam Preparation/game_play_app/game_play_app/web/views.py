from django.shortcuts import render, redirect

from game_play_app.web.forms import ProfileCreateForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from game_play_app.web.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.first()
    except:
        return None


def index(request):
    context = {
        'profile': get_profile(),
    }
    return render(request, 'core/home-page.html', context)


def dashboard(request):
    context = {
        'profile': get_profile(),
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
    profile = get_profile()
    games = Game.objects.all()
    total_games_count = games.count()
    average_rating = 0

    for game in games:
        average_rating += game.rating

    average_rating = average_rating / total_games_count

    context = {
        'profile': profile,
        'total_games_count': total_games_count,
        'average_rating': average_rating,
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)


def create_game(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'form': form,
    }

    return render(request, 'game/create-game.html', context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'profile': get_profile(),
        'game': game,
    }
    return render(request, 'game/details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'form': form,
        'game': game,
    }

    return render(request, 'game/edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': get_profile(),
        'game': game,
        'form': form,
    }

    return render(request, 'game/delete-game.html', context)
