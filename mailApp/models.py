from django.db import models
from django.core.exceptions import ValidationError
from .mails import send_final_mail
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

    confirmed = models.BooleanField(default=False)
    done = models.BooleanField(default=False,editable=False)
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            if((not self.done)and(self.confirmed)):
                send_final_mail(self.email)
                self.done = True
        except Exception as e:
            print(e)
        finally:
            return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.name
# Create your models here.