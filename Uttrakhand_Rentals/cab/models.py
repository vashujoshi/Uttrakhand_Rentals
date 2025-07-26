from django.db import models
from django.utils import timezone

class car_options(models.Model):  # ✅ Use PascalCase for class name
    CAR_TYPE_CHOICES = [
        ('mini', 'Mini'),
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('7seater', '7 Seater'),
    ]

    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)
    availability = models.BooleanField()
    image = models.ImageField(upload_to='cabs/')
    description = models.TextField(blank=True, null=True)

def __str__(self):
    return self.name