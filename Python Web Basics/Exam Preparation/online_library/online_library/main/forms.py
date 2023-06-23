from django import forms

from online_library.main.models import Profile, Book


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    pass


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CreateBookForm(BaseBookForm):
    pass


class EditBookForm(BaseBookForm):
    pass
