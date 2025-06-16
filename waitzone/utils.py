from django.core.mail import send_mail
from django.conf import settings

def send_waitlist_email(name, email):
    subject = "You're on the Waitlist!"
    message = f"""Hi {name or 'there'},\n\nThank you for joining the waitlist for ORU-UBI — an initiative we're passionately building to empower individuals through inclusive and sustainable innovation.\n\nYour interest means a lot to us as we continue developing this project and seeking the right partners and funding to bring it to life. We'll keep you updated on our progress, milestones, and how you can get involved as we move forward.\n\nIf you have any questions or would like to learn more in the meantime, feel free to reach out.\n\nWarm regards,\n\nThe ORU-UBI Team"""
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
