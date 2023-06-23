from django.shortcuts import render


def index(request):
    return render(request, 'core/home-no-profile.html')


def add_book(request):
    pass


def edit_book(request, pk):
    pass


def book_details(request, pk):
    pass


def profile_details(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass
