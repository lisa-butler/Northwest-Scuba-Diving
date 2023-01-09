from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

def contact(request):
    """ A view to return the contact page """
    form_data = {
            'first_name': request.POST.get('first_name'),
            'email': request.POST.get('email'),

        }
    contact_form = ContactForm(form_data)
    context = {'contact_form' : contact_form}
    return render(request, 'contact/contact.html', context)