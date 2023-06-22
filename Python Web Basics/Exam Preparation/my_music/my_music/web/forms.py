from django import forms

from my_music.web.models import Profile, Album


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }
            ),

            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),

            'Age': forms.TextInput(
                attrs={
                    'placeholder': 'Age'
                }
            ),
        }


class CreateProfileForm(BaseProfileForm):
    pass


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'
                }
            ),

            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),

            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                }
            ),

            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL'
                }
            ),

            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price'
                }
            ),
        }
        labels = {
            'album_name': 'Album Name',
            'image_url': 'Image URL',
        }


class AddAlbumForm(BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(BaseAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

