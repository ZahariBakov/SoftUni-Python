from django import forms

from my_music.web.models import Profile


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
