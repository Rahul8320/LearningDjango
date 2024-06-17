from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE)
    description = models.TextField(default="")
    price = models.IntegerField(default=10)

    def __str__(self):
        return self.name