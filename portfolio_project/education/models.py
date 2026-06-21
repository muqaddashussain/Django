from django.db import models

# Create your models here.

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.degree
