from django.db import models
from django.contrib.auth.models import User


class UserReviewForm(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    review = models.TextField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_review', related_query_name='user_review')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title