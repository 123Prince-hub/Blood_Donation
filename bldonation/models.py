from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField()