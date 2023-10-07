from django.db import models
from django.urls import reverse

# Create your models here.




class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    founded_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name
class teacher(models.Model):
    name=models.CharField(max_length=100)
    exp=models.IntegerField()
    subject=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('getteacher',kwargs={'pk':self.pk}) 
    def get_absolute_url(self):
        return reverse('listteacher') 


    
    
