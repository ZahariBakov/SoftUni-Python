from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.like_set.count()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    return render(request, template_name='photos/photo-edit-page.html')


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('home page')
