from django.shortcuts import render,redirect
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import datetime as dt
from django.shortcuts import get_object_or_404
# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.city

class Barber(models.Model):
    barber_name = models.CharField(max_length=30, blank=True)
    barber_shop_name = models.CharField(max_length=30, blank=True)
    location_id = models.ForeignKey(Location,blank=True, on_delete=models.CASCADE,related_name='location',null=True)
    business_email = models.EmailField(max_length=70,blank=True)
    work_sample = models.ImageField(upload_to = 'sample/',default="wati.jpeg")


    def __str__(self):
        return self.barber_name

    @classmethod
    def search_by_barber_name(cls,search_term):
        project = Barber.objects.filter(barber_name__icontains = search_term)
        return project


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    name = models.CharField(max_length=30, blank=True)
    email_address = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.name
        class Meta:
            ordering= ['user']

    def save_user(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender,instance, **kwargs):
        instance.profile.save()

class Post(models.Model):

    image_path = models.ImageField(upload_to = 'gallery/')
    image_description = models.CharField(max_length=100, blank=True)
