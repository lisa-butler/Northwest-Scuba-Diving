from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .forms import NewsletterSignupForm
from .models import Newsletter
from django.contrib import messages


def newsletter(request):
    """ A view to return the newsletter page """
    if request.method == 'POST':
        form_data = {
                'email': request.POST.get('email'),
            }
        newsletter_form = NewsletterSignupForm()(form_data)
        if newsletter_form.is_valid():
            newsletterSignupRequest = newsletter_form.save(commit=False)
            newsletterSignupRequest.save()

            request.session['save_newsletter_request'] = 'save_newsletter_request' in request.POST
            return redirect(reverse('newsletter_signup_success', args=[newsletterSignupRequest.email]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        newsletter_form = NewsletterSignupForm()
        context = {'newsletter_form': newsletter_form}
        return render(request, 'newsletter/newsletter.html', context)


def newsletter_signup_success(request, email):
    """
    Handle successful newsleter signup requests
    """
    save_newsletter_request = request.session.get('save_newsletter_request')
    newsletter = get_object_or_404(Newsletter, email=email)

    if request.user.is_authenticated:
        if save_newsletter_request:
            newsletter_form_data = {
                'email': newsletter.email,
            }
            newsletter_form = NewsletterSignupForm(newsletter_form_data, instance=newsletter)
            if newsletter_form.is_valid():
                newsletter_form.save()

    messages.success(request, f'Sucessfully Signed up to Northwest Scuba Diving Newsletter! \
        Your email address {newsletter.email} has been signed up to our newsletter.')

    template = 'newsletter/newsletter_signup_success.html'
    context = {
        'newsletter': newsletter,
    }

    return render(request, template, context)