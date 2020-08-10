from django.db import models
from django.urls import reverse

# Create your models here.


class timetable(models.Model):
    days = models.CharField(max_length=64)
    sub1= models.CharField(max_length=64)
    sub2 = models.CharField(max_length=64)
    sub3 = models.CharField(max_length=64)
    sub4= models.CharField(max_length=64)
    sub5 = models.CharField(max_length=64,blank="True")
    sub6 = models.CharField(max_length=64)
    sub7 = models.CharField(max_length=64)
    sub8 = models.CharField(max_length=64)

    def __str__(self):
        return self.days

    def get_absolute_url(self):
        return reverse("TT:list", kwargs={'pk': self.pk})
