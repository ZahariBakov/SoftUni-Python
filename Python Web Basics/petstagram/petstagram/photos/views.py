from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


@login_required
def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


@login_required
def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.like_set.count()
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


@login_required
def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    form = PhotoEditForm(request.POST or None, instance=photo)

    if form.is_valid():
        form.save()
        return redirect('photo details', pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


@login_required
def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('home page')
