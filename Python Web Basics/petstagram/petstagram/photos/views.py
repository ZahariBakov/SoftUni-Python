from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm
from petstagram.photos.models import Photo


class PhotoAddView(views.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoAddForm

    def get_success_url(self):
        return reverse('photo details', kwargs={
            'pk': self.object.pk
        })

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #
    #     return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user

        return form


# @login_required
# def add_photo(request):
#     form = PhotoCreateForm(request.POST or None, request.FILES or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('home page')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'photos/photo-add-page.html', context)


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
