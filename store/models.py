from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Customer(models.Model):
    username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phoneNumber=models.IntegerField()

class Food(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(decimal_places=2, max_digits=6)
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
    	try:
    		url = self.image.url
    	except:
    		url = ''
    	return url

    def get_absolute_url(self):
        return reverse("product", kwargs={
            "pk" : self.pk
        })

    def get_add_to_cart_url(self) :
        return reverse("add-to-cart", kwargs={
            "pk" : self.pk
        })

    def get_remove_from_cart_url(self) :
        return reverse("remove-from-cart", kwargs={
            "pk" : self.pk
        })

class Order(models.Model):
    username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null= True)
    #username=models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True)
    paid=models.BooleanField(default=False)
    order_number=models.CharField(max_length=100)
    items = models.ManyToManyField(Food)

    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

class OrderFood(models.Model):
    #username=models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True)
    username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null= True)
    food=models.ForeignKey(Food, on_delete=models.SET_NULL, null= True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} of {self.food.name}"
