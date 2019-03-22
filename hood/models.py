from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=30)
    hood = models.CharField(max_length=30)

    def __str__(self):
        return self.hood

class User(models.Model):
    name = models.CharField(max_length=30)
    id = models.IntegerField()
    neighborhood_id=models.ForeignKey(NeighbourHood,blank=True, on_delete=models.CASCADE,related_name='neighborhood',null=True)
    email address = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.name

class NeighbourHood (models.Model):
    neighbourhood_name = models.CharField(max_length=30)
    location_id = models.ForeignKey(Location,blank=True, on_delete=models.CASCADE,related_name='location',null=True)
    occupants_count = models.IntegerField()
    user_id = models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='neighborhood',null=True)

    def __str__(self):
        return self.neighbourhood_name


class Business(models.Model):
    business_name = models.CharField(max_length=30)
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='neighborhood',null=True)
    neighborhood_id = models.ForeignKey(NeighbourHood,blank=True, on_delete=models.CASCADE,related_name='neighborhood',null=True)
    business_email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.business_name
