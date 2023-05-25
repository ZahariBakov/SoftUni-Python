from django import forms

from car_collection_app.web.models import Profile, Car


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
