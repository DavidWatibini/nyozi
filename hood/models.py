from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=30, blank=True)
    hood = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.hood

class NeighbourHood (models.Model):
    neighbourhood_name = models.CharField(max_length=30, blank=True)
    location_id = models.ForeignKey(Location,blank=True, on_delete=models.CASCADE,related_name='location',null=True)
    user_id = models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='user',null=True)

    def __str__(self):
        return self.neighbourhood_name


class Business(models.Model):
    business_name = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='neighborhood',null=True)
    neighborhood_id = models.ForeignKey(NeighbourHood,blank=True, on_delete=models.CASCADE,related_name='neighborhood',null=True)
    business_email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.business_name

class User(models.Model):
    name = models.CharField(max_length=30, blank=True)
    email_address = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.name
