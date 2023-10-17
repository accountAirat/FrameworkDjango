from django.core.management.base import BaseCommand
from homework2app.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='Neo', email='neo@example.com', msisdn='7900000000', address='Kazan')
        user = User(name='John', email='john@example.com', msisdn='7900000000', address='Kazan')
        user.save()
        self.stdout.write(f'{user}')

