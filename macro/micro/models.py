from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()


class Products(models.Model):
    name = models.CharField(max_length=122)
    desc = models.TextField()
    price = models.IntegerField()
    images= models.ImageField(upload_to='products')
    

    def __str__(self):
        return self.name