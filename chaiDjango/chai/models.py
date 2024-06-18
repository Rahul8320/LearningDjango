from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default="")
    price = models.IntegerField(default=10)

    def __str__(self):
        return self.name
    
# one to many relationship
class ChaiReview(models.Model):
    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE,related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"

## many to many relationship
class ChaiStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name
    
### one to one relationship
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name="certificate")
    certificate_number = models.CharField(max_length=100, unique=True)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.chai.name}"