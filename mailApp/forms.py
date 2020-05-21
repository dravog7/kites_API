from .models import Registrant
from django.forms import ModelForm

class RegistrantForm(ModelForm):
    class Meta:
        model = Registrant
        fields = [
            'name',
            'email',
            'phone',
            'state',
            'district',
            'qualification',
            'occupation',
            'interest'
        ]