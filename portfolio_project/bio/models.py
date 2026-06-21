from django.db import models

# Create your models here.

class Bio(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name
