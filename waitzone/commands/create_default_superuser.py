
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a default superuser if not exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        if not User.objects.filter(username=os.environ('USERNAME')).exists():
            User.objects.create_superuser(
                username=os.environ('ADMIN_USERNAME'),
                email=os.environ('ADMIN_EMAIL'),
                password=os.environ('ADMIN_PASSWORD'),
            )
            self.stdout.write(self.style.SUCCESS("Superuser created"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))
