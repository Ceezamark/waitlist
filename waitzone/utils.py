from django.core.mail import send_mail
from django.conf import settings

def send_waitlist_email(name, email):
    subject = "You're on the Waitlist!"
    message = f"Hi {name or 'there'},\n\nThanks for joining our waitlist. We'll be in touch soon!"

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
