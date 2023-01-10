from django.shortcuts import render


# Create your views here.
def sample_view(request, *args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
