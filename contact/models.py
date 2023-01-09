from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=75, null=False, blank=False)
    email = models.CharField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name
