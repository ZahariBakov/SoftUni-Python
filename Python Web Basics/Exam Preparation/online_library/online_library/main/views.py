from django.shortcuts import render, redirect

from online_library.main.forms import CreateProfileForm, CreateBookForm, EditBookForm
from online_library.main.models import Book
from online_library.processors import get_profile


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
    profile = get_profile

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
    book = Book.objects.filter(pk=pk)
    form = EditBookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }

    return render(request, 'book/edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.filter(pk=pk)

    context = {
        'book': book,
    }

    return render(request, 'book/book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk)
    book.delete()

    return redirect('index')


def profile_details(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass
