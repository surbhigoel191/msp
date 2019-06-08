from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Candidate(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.URLField(default='')
    bitsid = models.TextField()
    contact = models.IntegerField(default=0)
    

    