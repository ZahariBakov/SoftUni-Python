from django import forms

from my_plant_app.main.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name')


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
