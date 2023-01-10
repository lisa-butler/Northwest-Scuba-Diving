from django.db import models
import uuid


class Contact(models.Model):
    ticket_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=75, null=False, blank=False)
    email = models.CharField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name

    def _generate_ticket_number(self):
        """
        Generate a random, unique ticket number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = self._generate_ticket_number()
        super().save(*args, **kwargs)
