from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reservation(models.Model):
    event_name = models.TextField()
    event_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['-event_date']

