from django.db import models

# Create your models here.




class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    founded_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

    
    
