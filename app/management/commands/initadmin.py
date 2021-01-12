
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import os


class Command(BaseCommand):

    def handle(self, *args, **options):

        username = 'wasuaje'
        email = 'wasuaje@gmail.com'
        password = os.environ['django_adminpass']
        print('Creating account for %s (%s)' % (username, email))
        User.objects.filter(email=email).delete()
        admin = User.objects.create_superuser(
            email=email, username=username, password=password)
        admin.is_active = True
        admin.is_admin = True
        admin.save()
