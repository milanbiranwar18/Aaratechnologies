from django.db import models
from django.db.models import JSONField
from user.models import User


class Shop(models.Model):
    name = models.CharField(max_length=200)
    location = JSONField()
    description = models.TextField()


class Review(models.Model):
    shop = models.ForeignKey(Shop, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

