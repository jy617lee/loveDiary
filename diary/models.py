from django.db import models
from django.utils import timezone

# Create your models here.
class Posting(models.Model):
    text = models.CharField(max_length = 500)
    update_date = models.DateField()

    def generate(self):
        self.update_date = timezone.now()
        self.save()
