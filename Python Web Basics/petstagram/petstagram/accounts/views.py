from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from petstagram.accounts.forms import RegisterUserForm
from petstagram.pets.models import Pet


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'

    # success_url =
    # def get_success_url(self):


class LogoutUserView(auth_views.LogoutView):
    pass


def show_profile_details(request, pk):
    pets = Pet.objects.all()

    context = {
        'pets': pets,
    }

    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
