from django import forms

from petstagram.photos.models import Photo

labels = {
    'photo': 'Photo file',
    'tagged_pets': 'Tag Pets',
}


class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']
        labels = labels


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']
        labels = labels
