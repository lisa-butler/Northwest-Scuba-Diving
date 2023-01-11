from django.db import models
import uuid


class Newsletter(models.Model):
    email = models.CharField(max_length=254, null=False, blank=False)


    def __str__(self):
        return self.name

    # def _generate_ticket_number(self):
    #     """
    #     Generate a random, unique ticket number using UUID
    #     """
    #     return uuid.uuid4().hex.upper()

    # def save(self, *args, **kwargs):
    #     if not self.ticket_number:
    #         self.ticket_number = self._generate_ticket_number()
    #     super().save(*args, **kwargs)
