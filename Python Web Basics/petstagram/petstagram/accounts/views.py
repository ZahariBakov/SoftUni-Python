from django.shortcuts import render

from petstagram.pets.models import Pet


def register(request):
    return render(request, template_name='accounts/register-page.html')


def login(request):
    return render(request, template_name='accounts/login-page.html')


def show_profile_details(request, pk):
    pets = Pet.objects.all()

    context = {
        'pets': pets,
    }

    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
