from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

# Breed Model
class Breed(models.Model):
    TINY = 'tiny'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    BREED_SIZE_CHOICES = [
        (TINY, 'tiny'),
        (SMALL, 'small'),
        (MEDIUM, 'medium'),
        (LARGE, 'large'),
    ]
    size = models.CharField(
        max_length=6,
        choices=BREED_SIZE_CHOICES,
        default=TINY,
    )

    name = models.CharField(max_length=50, blank=False)
    # (a character string) [should accept Tiny, Small, Medium, Large]
    friendliness = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]
    trainability = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]
    sheddingamount = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]
    exerciseneeds = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    # (an integer field) [should accept values from 1-5]

    def __str__(self):
        return str(self.name)

# Dog model
class Dog(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=False)
    color = models.CharField(max_length=30, blank=False)
    favoriteFood = models.CharField(max_length=50, blank=False)
    favoriteToy = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.name)