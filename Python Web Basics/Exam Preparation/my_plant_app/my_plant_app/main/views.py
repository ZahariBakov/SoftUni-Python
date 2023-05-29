from django.shortcuts import render


def get_profile():
    return 'Have a profile'
    # return None


def index(request):
    profile = get_profile

    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def catalogue(request):
    return render(request, 'catalogue.html')


def profile_create(request):
    return render(request, 'create-profile.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def profile_edit(request):
    return render(request, 'edit-profile.html')


def profile_delete(request):
    return render(request, 'delete-profile.html')


def plant_create(request):
    return render(request, 'create-plant.html')


def plant_details(request):
    return render(request, 'plant-details.html')


def plant_edit(request):
    return render(request, 'edit-plant.html')


def plant_delete(request):
    return render(request, 'delete-plant.html')
