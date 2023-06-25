from django import forms

from fruitipedia_app.web.models import Profile, Fruit


class CreatProfileForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),

            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),

            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Password'
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image_url', 'age']

    first_name = forms.CharField(label='First Name:')
    last_name = forms.CharField(label='Last Name:')
    image_url = forms.CharField(label='Image URL:')
    age = forms.CharField(label='Age:')


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }
            ),

            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),

            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),

            'nutrition': forms.TextInput(
                attrs={
                    'placeholder': 'Nutrition Info'
                }
            ),
        }


class CreateFruitForm(BaseFruitForm):
    pass


class EditFruitForm(BaseFruitForm):
    name = forms.CharField(label='Name:')
    image_url = forms.CharField(label='Image URL:')
    description = forms.CharField(label='Description:')
    nutrition = forms.CharField(label='Nutrition:')


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.disabled = True
            field.required = False
