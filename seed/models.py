from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

#we will create 8 models (means tables )
class User(AbstractUser):
    phone_number = models.IntegerField( blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="seed_user_groups",  # Add a unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="seed_user_permissions",  # Add a unique related_name
        blank=True
    )

    def __str__(self):
        return self.username


class Seed(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    image = models.ImageField(upload_to='seed/')
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i,i) for i in range (1,6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username}"


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items.all()) 
    


class CartItem(models.Model):
    cart = models.ForeignKey(Cart , related_name='items' , on_delete=models.CASCADE)
    seed = models.ForeignKey(Seed , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_subtotal(self):
        return self.seed.price * self.quantity
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amout = models.DecimalField(max_digits=10 , decimal_places=2)
    shipping_address = models.TextField()
    status = models.CharField(max_length=20 , choices=STATUS_CHOICES , default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    price = models.DecimalField(max_digits = 10 , decimal_places=2)

    def get_total(self):
        return self.quantity * self.price
    





