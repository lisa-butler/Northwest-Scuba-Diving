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

def message_sent(request):
    """ A view to return the message_sent page """

    return render(request, 'home/message_sent.html')


def newsletter_confirmation(request):
    """ A view to return the newsletter_confirmation page """

    return render(request, 'home/newsletter_confirmation.html')