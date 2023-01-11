from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .forms import NewsletterSignupForm
from .models import Newsletter
from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages

def get_all_objects(model):
    queryset = model._meta.model.objects.all()
    return queryset


def newsletter(request):
    """ A view to return the newsletter page """
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        user = get_object_or_404(User, username=profile.user)
        user_email = user.email
        email_registered = get_all_objects(Newsletter).filter(email=user_email)

        if request.method == 'POST':
            if email_registered is None or not email_registered:
                print("New Signup Attempt")
                form_data = {
                        'email': user_email
                    }
                newsletter_form = NewsletterSignupForm(form_data)
                newsletterSignupRequest = newsletter_form.save(commit=False)
                newsletterSignupRequest.save()
                request.session['save_newsletter_request'] = 'save_newsletter_request' in request.POST
                return redirect(reverse('newsletter_signup_success', args=[newsletterSignupRequest.email]))
            else:
                request.session['unsubscribe_newsletter_request'] = 'unsubscribe_newsletter_request' in request.POST
                return redirect(reverse('newsletter_unsubscribe', args=[user_email]))
        else:
            context = {'email': email_registered}
            return render(request, 'newsletter/newsletter.html', context)
    else:
        return render(request, 'newsletter/newsletter.html')


def newsletter_signup_success(request, email):
    """
    Handle successful newsleter signup requests
    """
    # save_newsletter_request = request.session.get('save_newsletter_request')

    if request.user.is_authenticated:
        print("Got into signup sucess")

    #     # if save_newsletter_request:
    #     newsletter_form_data = {
    #         'email': email,
    #     }
    #     newsletter_form = NewsletterSignupForm(newsletter_form_data, instance=newsletter)
    #     if newsletter_form.is_valid():
    #         newsletter_form.save()

    messages.success(request, f'Sucessfully Signed up to Northwest Scuba Diving Newsletter! \
        Your email address {email} has been signed up to our newsletter.')

    template = 'newsletter/newsletter_signup_success.html'
    # template = 'newsletter/newsletter_unsubscribe.html'
    context = {
        'email': email,
    }

    return render(request, template, context)


def newsletter_unsubscribe(request, email):
    """
    Handle successful newsleter unsubscribe requests
    """
    newsletter = get_all_objects(Newsletter).filter(email=email)

    if request.user.is_authenticated:
        newsletter.delete()

    messages.success(request, f'Sucessfully unsubscribed from Northwest Scuba Diving Newsletter! \
        Your email address {email} has been unsubscribed from our newsletter.')

    template = 'newsletter/newsletter_unsubscribe.html'
    context = {
        'email': email,
    }

    return render(request, template, context)