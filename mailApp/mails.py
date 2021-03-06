from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

FROM_EMAIL = "Kites Foundation <info@kitesfoundation.org>" #must verify sender id before using

def sendgrid_mail_error_handler(func):
    def f(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except Exception as e: #replace with handlers for each sendgrid error
            print(str(e))
            raise Exception(str(e))
    return f

@sendgrid_mail_error_handler
def send_welcome_mail(to_mail,**kwargs):
    mail = EmailMultiAlternatives(
        subject="Your Subject",
        body="This is a simple text email body.",
        from_email=FROM_EMAIL,
        to=[to_mail],
    )
    mail.template_id = 'd-c40ad5d0f3a24a7e8dc79f8850d3ef12'
    # mail.substitutions = kwargs
    mail.attach_alternative("<p>a</p>", "text/html")
    mail.send()