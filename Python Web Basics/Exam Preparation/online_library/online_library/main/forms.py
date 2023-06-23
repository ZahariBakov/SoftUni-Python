from django import forms

from online_library.main.models import Profile, Book


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for filed in self.fields.values():
            filed.disabled = True
            filed.required = False


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CreateBookForm(BaseBookForm):
    pass


class EditBookForm(BaseBookForm):
    pass
