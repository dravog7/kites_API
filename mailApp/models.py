from django.db import models
from django.core.exceptions import ValidationError
def validate_phone(value):
    if len(str(value))>=10:
        return
    raise ValidationError('{0} is not a phone number'.format(value))

class Registrant(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(validators=[validate_phone])
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    qualification= models.TextField(default='',blank=True)
    occupation = models.CharField(max_length=500,default='',blank=True)
    interest = models.CharField(max_length=500,default='',blank=True)

    def __str__(self):
        return self.name
# Create your models here.