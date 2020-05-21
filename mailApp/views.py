from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden,HttpResponseServerError
from django.db import IntegrityError
from .models import Registrant
from .mails import send_welcome_mail
from .forms import RegistrantForm

@csrf_exempt
def register(req):
    #process registration
    name,email,phone= [None]*3
    form = None
    #replace with model form
    try:
        form = RegistrantForm(req.POST)
        if not form.is_valid():
            raise Exception()
    except:
        return HttpResponseBadRequest(form.errors.as_text())
    
    form.save()

    #send mail
    try:
        send_welcome_mail(form.cleaned_data['email'])
    except:
        return HttpResponseServerError("sending email failed")
    return HttpResponse(content='Success!')