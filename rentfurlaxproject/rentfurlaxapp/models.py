from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Register(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=40,unique=True)
    phone = models.CharField(max_length=12,unique=True)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=12,unique=True)

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.username},{self.email},{self.phone},{self.address}"
       
class Category(models.Model):
    type= models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.type

class Product(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField()
    condition= models.CharField(max_length=255)
    noofdays= models.IntegerField()
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    options= models.JSONField()
    rentaloptions= models.JSONField()

    def __str__(self):
        return self.name

class Invoice(models.Model):
    user= models.ForeignKey(Register, on_delete=models.CASCADE) 
    products = models.ManyToManyField(Product)
    status= models.CharField(max_length=50, choices=[
        ('ORDERED','ordered'),
        ('CANCELLED', 'cancelled'),
        ('DELIVERED', 'delivered'),
    ])  
    total_amount= models.DecimalField(max_digits=10, decimal_places=2)