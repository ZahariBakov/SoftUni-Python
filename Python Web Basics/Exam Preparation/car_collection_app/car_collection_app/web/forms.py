from django import forms


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
