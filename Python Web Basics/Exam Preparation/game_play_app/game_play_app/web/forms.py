from django import forms

from game_play_app.web.models import Profile


class ProfileCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
