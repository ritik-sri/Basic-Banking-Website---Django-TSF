from django.db import models

# Create your models here.
class Balance(models.Model):
  
    # fields of the model
    name = models.CharField(max_length = 300)
    bankid = models.IntegerField()
    balance=models.IntegerField()
    email=models.CharField(max_length=300)