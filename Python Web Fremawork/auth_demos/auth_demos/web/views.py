import random

from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect

UserModel = get_user_model()


def index(request):
    # user = UserModel(
    #     username='Zahari',
    #     password='1123QwER',
    # )
    # user.save()

    suffix = random.randint(1, 1000)

    # Create and saves
    # Not a good idea to create а user this way.
    # Saves password in plain text
    # UserModel.objects.create(
    #     username=f'Zahari_{suffix}',
    #     password='1123QwER',
    # )

    # This is the correct way to create user
    user = UserModel.objects.create_user(
        username=f'Zahari_{suffix}',
        password='1123QwER',
    )

    # print('-' * 20)
    # print(request.user)
    # login(request, user)
    # print(request.user)
    # print('-' * 20)
    # admin = UserModel.objects.get(username='admin')

    context = {
        'user': request.user,
    }

    return render(request, 'index.html', context)


def login_user(request):
    # Authentication
    user = authenticate(
        username='Zahari_397',
        password='1123QwER',
    )

    # Authorization
    login(request, user) # Does `request.user = user` + other stuff

    print(f'Authenticated user: {user}')

    return redirect('index')
