import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    message = models.TextField(null=False,blank=False)
    def __str__(self):
        return self.email

class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name