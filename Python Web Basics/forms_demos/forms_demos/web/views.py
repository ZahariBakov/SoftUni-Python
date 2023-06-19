from django.shortcuts import render

from forms_demos.web.forms import PersonForm, PersonModelForm
from forms_demos.web.models import Person


def index_form(request):
    name = None

    if request.method == 'GET':
        form = PersonForm()
    else: # request.method == 'post':
        form = PersonForm(request.POST)
        if form.is_valid():
            '''
            `is_valid()`:
            - validates the form, returns `True` or `False`
            - create `cleaned_data`
            - fills `cleaned_data`
            '''
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name,
            )

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context)


def index_model_form(request):
    instance = Person.objects.get(pk=1)

    if request.method == 'GET':
        form = PersonModelForm(instance=instance)
    else:
        form = PersonModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save() # Same as below
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            #
            # person.pets.set(pets)
            # person.save()

    context = {
        'form': form,
    }

    return render(request, 'model_forms.html', context)
