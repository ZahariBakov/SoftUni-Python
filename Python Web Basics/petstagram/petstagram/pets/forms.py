from django import forms
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']
        # fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Pet name",
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),

            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
        }

        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of birth',
            'personal_photo': 'Link to image',
        }


class PetAddForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(forms.ModelForm):
    pass
