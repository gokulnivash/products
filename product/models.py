from django.contrib.auth.models import User
from django.db import models

ROLE_TYPE = (('Admin','Admin'),('User','User'))
ACCESS_TYPE = (('Edit','Edit'),('View','View'))
# Create your models here.

class LoginRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role_type = models.CharField(max_length=30, blank=False, null=False, choices=ROLE_TYPE)
    access_type = models.CharField(max_length=30, blank=False, null=False, choices=ACCESS_TYPE)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=32, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=32, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)
