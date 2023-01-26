from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class UserReviewForm(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    review = models.TextField(max_length=400, null=False, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_review',
        related_query_name='user_review')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        username = None
        for key, value in kwargs.items():
            if key == "username":
                username = value
        loggedInUser = get_object_or_404(User, username=username)
        self.user = loggedInUser
        super().save()
