from django.shortcuts import render, redirect

from online_library.main.forms import CreateProfileForm, CreateBookForm, EditBookForm, EditProfileForm, \
    DeleteProfileForm
from online_library.main.models import Book, Profile


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'core/home-no-profile.html', context)


def index(request):
    profile = Profile.objects.first()

    if not profile:
        return redirect('create profile')

    context = {
        'books': Book.objects.all(),
    }

    return render(request, 'core/home-with-profile.html', context)


def add_book(request):
    form = CreateBookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'book/add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    form = EditBookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'book/edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get()

    context = {
        'book': book,
    }

    return render(request, 'book/book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()

    return redirect('index')


def profile_details(request):
    return render(request, 'profile/profile.html')


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    books = Book.objects.all()

    form = DeleteProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        books.delete()
        return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)

