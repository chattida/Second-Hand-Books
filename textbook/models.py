from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    text_book = models.CharField(max_length=255)
    TYPES = (
        ('1', 'sell'),
        ('2', 'buy')
    )
    type = models.CharField(max_length=1, choices=TYPES)
    price = models.FloatField()
    picture = models.ImageField(null=True)
    STATUSS = (
        ('1', 'open'),
        ('2', 'closed')
    )
    status = models.CharField(max_length=1, choices=STATUSS, default='1')
