from django.db import models

# Create your models here.
class Posting(models.Model):
    text = models.CharField(max_length = 500)
    update_date = models.DateField()
