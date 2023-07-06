from django.shortcuts import render, redirect
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


def add_pet(request):
    form = PetAddForm()

    if request.method == 'POST':
        form = PetAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    form = PetEditForm(request.POST, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('pet details', username=username, pet_name=pet_name)

    context = {
        'form': form,
        'pet_name': pet_name,
        'username': username,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')
