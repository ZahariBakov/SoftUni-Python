from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy
from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


def show_home_page(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    for photo in all_photos:
        photo.liked_by_user = photo.like_set\
            .filter(user=request.user)\
            .exists()

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)

    kwargs = {
        'to_photo': photo,
        'user': request.user
    }

    like_object = Like.objects\
        .filter(**kwargs)\
        .first()

    if like_object:
        like_object.delete()
    else:
        new_like_object = Like(**kwargs)
        new_like_object.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def comment_functionality(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.filter(pk=photo_id).get()
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.to_photo = photo
            new_comment.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")
