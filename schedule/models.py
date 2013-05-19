from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    user = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)

    def ___unicode___(self):
        return self.title


