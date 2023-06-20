from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpResponse
from django.shortcuts import render

from forms_demos_part_2.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(
            validate_text,
        ),
    )

    is_done = forms.BooleanField(
        required=False,
    )

    priority = forms.IntegerField(
        validators=(
            # validate_priority,

            # MinValueValidator(1),
            # MaxValueValidator(10),

            ValueInRangeValidator(1, 10),
        ),
    )

    # def clean_text(self):
    #     pass
    #
    # def clean_priority(self):
    #     pass
    #
    # def clean_is_done(self):
    #     pass


def index(request):
    if request.method == 'GET':
        form = TodoForm()
    else:
        form = TodoForm(request.POST)

    if form.is_valid():
        return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)
