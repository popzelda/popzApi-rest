from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=50)
    content= models.TextField()
    price= models.FloatField()
    def __str__(self):
        return self.name
    #@property
    #def get_desc(self):
       #    return self.name
   