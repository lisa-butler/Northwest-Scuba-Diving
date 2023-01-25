from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from .forms import ContactForm
from .models import Contact
from django.contrib import messages


def contact(request):
    """ A view to return the contact page """
    if request.method == 'POST':
        form_data = {
                'first_name': request.POST.get('first_name'),
                'email': request.POST.get('email'),
                'subject': request.POST.get('subject'),
                'message': request.POST.get('message'),
            }
        contact_form = ContactForm(form_data)
        if contact_form.is_valid():
            contactRequest = contact_form.save(commit=False)
            contactRequest.save()

            request.session['save_contact_request'] = 'save_contact_request' in request.POST
            return redirect(reverse('contact_request_success',
                            args=[contactRequest.ticket_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'contact/contact.html', context)


def contact_request_success(request, ticket_number):
    """
    Handle successful contact requests
    """
    save_contact_request = request.session.get('save_contact_request')
    contact = get_object_or_404(Contact, ticket_number=ticket_number)

    if request.user.is_authenticated:
        if save_contact_request:
            contact_form_data = {
                'first_name': contact.first_name,
                'email': contact.email,
                'subject': contact.subject,
                'message': contact.message,
            }
            contact_form = ContactForm(contact_form_data, instance=contact)
            if contact_form.is_valid():
                contact_form.save()

    messages.success(request, f'Message successfully sent! \
        Your message about {contact.subject} has been sent. We will respond to {contact.email}.')

    template = 'contact/contact_request_success.html'
    context = {
        'contact': contact,
    }

    return render(request, template, context)
