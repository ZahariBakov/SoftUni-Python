from django.shortcuts import render

from petstagram.photos.models import Photo


def add_photo(request):
    return render(request, template_name='photos/photo-add-page.html')


def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request):
    return render(request, template_name='photos/photo-edit-page.html')
