from django.db import models

# Create your models here.

class categorie(models.Model):
    name=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(categorie, on_delete=models.CASCADE, default=0)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    # image =  models.ImageField(upload_to = 'images/')
    def __str__(self):
        return self.name