
from django.db import models

# Create your models here.


# class BlogInfo(models.Model) :
#    title = models.CharField(max_length=20)
#    date = models.CharField(max_length=10)
#    description = models.CharField(max_length=52)
#    url = models.URLField(blank=True)

class Blog(models.Model) :
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self) :
        return self.title