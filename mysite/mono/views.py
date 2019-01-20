from django.shortcuts import render
from django.http import HttpResponse
from .forms import initial_form
from django.core import validators
from .core import *


# Create your views here.

def serve_image(request, filename):
    # print(filename)
    with open('mono/generated/' + filename, "rb") as f:
        return HttpResponse(f.read(), content_type='image/png')


def generate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = initial_form(request.POST)
        if form.is_valid():
            initials = str(form.cleaned_data['initials']).upper()
            font = str(form.cleaned_data['font'])
            image = Core.render_image(initials, font)
            print("path=" + image)
            context = {
                'initials': initials,
                'font': font,
                'image': image,
                'form': form,
            }
            return render(request, 'mono/generate.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        # Set Defaults
        form = initial_form()
        initials = ''
        font = ''
        image = '../../static/mono/preview_monogram.png'

        context = {
            'initials': initials,
            'font': font,
            'image': image,
            'form': form,
        }
        return render(request, 'mono/generate.html', context)
        # return HttpResponse('You\'re generating a monogram for the initials: %s.' % str(initials).upper())
