from django.db import models

# Create your models here.


class OrderPizza(models.Model):
    pizzatype = (
        ('Regular', 'Regular'),
        ('Square', 'Square'),
    )

    pizzasize = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )

    pizzatoopings = (
        ('Onion', 'Onion'),
        ('Tomato', 'Tomato'),
        ('Corn', 'Corn'),
        ('Capsicum', 'Capsicum'),
        ('Cheese', 'Cheese'),
        ('Jalapeno', 'Jalapeno')
    )
    Type = models.CharField(max_length=8, choices=pizzatype, default='Regular')
    Size = models.CharField(max_length=8, choices=pizzasize, default='Medium')
    Added = models.CharField(max_length=8, choices=pizzatoopings, default='Cheese')

    def __str__(self):
        return self.Type

    class Meta:
        verbose_name_plural = 'OrderPizza'
