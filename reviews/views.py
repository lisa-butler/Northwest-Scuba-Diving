from django.shortcuts import render
from .forms import UserReviewForm
from .models import UserReviewForm
from django.contrib import messages

def reviews(request):
    """ A view to return the reviews page """

    return render(request, 'reviews/reviews.html')


def reviews(request):
    """ A view to return the reviews page """
    if request.method == 'POST':
        form_data = {
                'title': request.POST.get('title'),
                'review': request.POST.get('review'),
                'user': request.POST.get('user'),
                'created': request.POST.get('created'),

            }
        user_review_form = UserReviewForm(form_data)
        if user_review_form.is_valid():
            reviewSubmit = user_review_form.save(commit=False)
            reviewSubmit.save()

            request.session['save_review_submit'] = 'save-review-submit' in request.POST
            return redirect(reverse('review_post_success', args=[user_review_form.title]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        user_review_form = UserReviewForm()
        context = {'user_review_form': user_review_form}
        return render(request, 'reviews/reviews.html', context)