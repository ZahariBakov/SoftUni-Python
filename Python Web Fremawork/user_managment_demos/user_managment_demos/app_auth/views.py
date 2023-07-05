# app_auth/views.py
from django import forms
from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import forms as auth_forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(auth_forms.UserCreationForm):
    content = forms.BooleanField()

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = _('It works!')


class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm

    # Static way of providing `success_url`
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    # def get_form_class(self):
    #     if condition1:
    #         return Condition1Form
    #     elif condition2:
    #         return Condition2Form
    #     else:
    #         return Condition3Form

    # Dynamic way of providing `success_url`
    # def get_success_url(self):
    #     pass


class LoginUserView(auth_views.LoginView):
    template_name = 'app_auth/login.html'


class LogoutUserView(auth_views.LogoutView):
    pass


UserModel = get_user_model()


class ViewPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = 'app_auth/users_list.html'


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'
