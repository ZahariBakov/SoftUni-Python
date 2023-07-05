import random

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

UserModel = get_user_model()


@login_required
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

    Zahari_1000 = UserModel.objects.get(username='Zahari_1000')

    context = {
        'user': request.user,
        'permission': request.user.has_perm('auth.view_user'),
        'zahari_1000': Zahari_1000.has_perm('auth.view_user'),
    }

    return render(request, 'index.html', context)


class IndexView(views.TemplateView, LoginRequiredMixin):
    template_name = 'index.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        pass


def login_user(request):
    # Authentication
    user = authenticate(
        username='Zahari_397',
        password='1123QwER',
    )

    # Authorization
    login(request, user)  # Does `request.user = user` + other stuff

    print(f'Authenticated user: {user}')

    return redirect('index')


def logout_user(request):
    logout(request)

    return redirect('index')
