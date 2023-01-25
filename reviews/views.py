from django.shortcuts import render, redirect, reverse
from .forms import Review
from .models import UserReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def submit_review(request):
    """ A view to return the submit_review page """
    if request.method == 'POST':
        form_data = {
                'title': request.POST.get('title'),
                'review': request.POST.get('review'),

            }
        user_review_form = Review(form_data)
        if user_review_form.is_valid():
            reviewSubmit = user_review_form.save(commit=False)
            reviewSubmit.save(username=request.user)
            request.session['save_review_submit'] = 'save-review-submit' in request.POST
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        user_review_form = Review()
        context = {'user_review_form': user_review_form}
        return render(request, 'reviews/submit_review.html', context)


def get_all_objects(model):
    queryset = model._meta.model.objects.all()
    return queryset


def reviews(request):
    reviews = get_all_objects(UserReviewForm)
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)
