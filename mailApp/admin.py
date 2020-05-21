from django.contrib import admin
from .models import Registrant
# Register your models here.
@admin.register(Registrant)
class RegistrantAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone')