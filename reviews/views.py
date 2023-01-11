from django.shortcuts import render
from .forms import Review
from .models import UserReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def reviews(request):
    """ A view to return the reviews page """

    return render(request, 'reviews/reviews.html')

@login_required
def submit_review(request):
    """ A view to return the submit_review page """
    if request.method == 'POST':
        form_data = {
                'title': request.POST.get('title'),
                'review': request.POST.get('review'),
                'user': request.POST.get('user'),
                'created': request.POST.get('created'),

            }
        user_review_form = Review(form_data)
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
        return render(request, 'reviews/submit_review.html', context)


def get_all_objects(model):
    queryset = model._meta.model.objects.all()
    return queryset


def reviews(request):
    reviews = get_all_objects(Review)
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)