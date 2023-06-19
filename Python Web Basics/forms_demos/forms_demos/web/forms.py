from django import forms

from forms_demos.web.models import Person


class PersonForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High school student'),
        (3, 'Student'),
        (4, 'Adult'),
    )

    your_name = forms.CharField(
        max_length=30,
        label='Name',
        help_text='Enter your name',
        widget=forms.TextInput(
            # This corresponding to HTML attributes
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            },
        )
    )

    age = forms.IntegerField(
        required=False,
        initial=0,
        help_text='Enter your age',
        # This is the default for `IntegerField`
        # widget=forms.NumberInput(),
    )

    # email = forms.CharField(
    #     widget=forms.EmailInput(),
    # )
    #
    # url = forms.CharField(
    #     widget=forms.URLInput(),
    # )
    #
    # secret = forms.CharField(
    #     widget=forms.PasswordInput(),
    # )
    #
    # story = forms.CharField(
    #     widget=forms.Textarea()
    # )

    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        # This is the default for `ChoiceFiled`:
        widget=forms.Select,
    )

    # occupancy2 = forms.ChoiceField(
    #     choices=OCCUPANCIES,
    #     widget=forms.RadioSelect(),
    # )
    #
    # occupancy3 = forms.ChoiceField(
    #     choices=OCCUPANCIES,
    #     widget=forms.SelectMultiple(),
    # )

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'cols': 80, 'rows': 20,
                'class': 'special',
                'title': 'Add a comment'
            },
        )
    )


class PersonModelForm(forms.ModelForm):
    # story = forms.CharField(
    #     widget=forms.Textarea(),
    # )

    class Meta:
        model = Person
        fields = '__all__'
        # fields = ('name', 'age') # witch field include
        # exclude = ('age',) # witch field exclude
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

        help_texts = {
            'name': 'Your name',
        }

        labels = {
            'age': 'The AGE',
        }
