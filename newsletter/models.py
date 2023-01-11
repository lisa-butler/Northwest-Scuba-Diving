from django.db import models


class Newsletter(models.Model):
    email = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email
