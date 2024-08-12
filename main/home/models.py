from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    profile_img = models.ImageField(upload_to="user/profile_imgs")
    
    def __str__(self):
        return self.name
    
class Items(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=15)
    item_cost = models.IntegerField()
    item_img = models.ImageField(upload_to="shop/item_imgs")
    