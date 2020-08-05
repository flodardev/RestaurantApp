from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Topping
class Topping(models.Model):
    topping = models.CharField(max_length=69)
    def __str__(self):
        return self.topping

# Regular Pizza
class PizzaType(models.Model):
    menu = models.CharField(max_length=69, default=str, blank=True)
    def __str__(self):
        return self.menu

# Pizza
class Pizza(models.Model):
    name = models.CharField(max_length=69, default=str, blank=True)
    menu = models.ManyToManyField(PizzaType)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    topping_count = models.IntegerField(blank=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    def __str__(self):
        return self.name

# Subs
class Sub(models.Model):
    menu = models.CharField(max_length=69)
    extra_count = models.IntegerField(blank=True)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.menu

# Pasta
class Pasta(models.Model):
    menu = models.CharField(max_length=69)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.menu

# Salads
class Salad(models.Model):
    menu = models.CharField(max_length=69)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.menu

# Dinner Platters
class DinnerPlatter(models.Model):
    menu = models.CharField(max_length=69)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.menu

# Extras
class Extra(models.Model):
    menu = models.CharField(max_length=69)
    name = models.CharField(max_length=69)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.name

# Orders placed
class CustomerOrder(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivering', 'Delivering'),
        ('Delivered', 'Delivered')
    ]
    customer = models.CharField(max_length=69, blank=True, null=True)
    item = models.CharField(max_length=69, blank=True, null=True)
    name = models.CharField(max_length=69, blank=True, null=True)
    size = models.CharField(max_length=69, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    topping1 = models.CharField(max_length=69, blank=True, null=True)
    topping2 = models.CharField(max_length=69, blank=True, null=True)
    topping3 =  models.CharField(max_length=69, blank=True, null=True)
    extra1 = models.CharField(max_length=69, blank=True, null=True)
    extra2 = models.CharField(max_length=69, blank=True, null=True)
    extra3 = models.CharField(max_length=69, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer
