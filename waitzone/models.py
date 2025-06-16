from django.db import models
from django.utils.timezone import now

# Create your models here.

class WaitListSubscription(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)
    joined_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.email
