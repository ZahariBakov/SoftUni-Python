from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


@login_required
def add_pet(request):
    form = PetAddForm()

    if request.method == 'POST':
        form = PetAddForm(request.POST)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()

            return redirect('profile details', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


@login_required
def pet_details(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html', context)


@login_required
def edit_pet(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()

    form = PetEditForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('pet details', username=username, pet_name=pet_name)

    context = {
        'form': form,
        'pet_name': pet_name,
        'username': username,
    }

    return render(request, 'pets/pet-edit-page.html', context)


@login_required
def delete_pet(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            # pet.delete()
        return redirect('profile details', pk=1)

    context = {
        'form': form,
        'username': username,
        'pet_name': pet_name,
    }

    return render(request, 'pets/pet-delete-page.html', context)
