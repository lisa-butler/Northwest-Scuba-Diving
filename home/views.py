from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def get_in_contact(request):
    """ A view to return the get_in_contact page """

    return render(request, 'home/get_in_contact.html')