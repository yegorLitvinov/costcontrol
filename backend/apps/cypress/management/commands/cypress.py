from contextlib import contextmanager

from django.core.management.base import BaseCommand, CommandError

from apps.accounts.factories import UserFactory
from apps.accounts.models import User
from apps.costcontrol.factories import ProceedCategoryFactory, SpendingCategoryFactory

EMAIL = 'test@example.com'


@contextmanager
def command_error_context():
    try:
        yield
    except Exception as error:
        raise CommandError(error)


class Command(BaseCommand):
    help = 'Preparing for cypress tests.'

    def _adduser(self):
        user = UserFactory.build(email=EMAIL)
        user.set_password('password123')
        with command_error_context():
            user.save()

    def _rmuser(self):
        User.objects.get(email=EMAIL).delete()

    def _add_categories(self):
        with command_error_context():
            user = User.objects.get(email=EMAIL)
        ProceedCategoryFactory(user=user)
        SpendingCategoryFactory(user=user)

    def add_arguments(self, parser):
        parser.add_argument(
            '--adduser',
            dest='adduser',
            type=bool,
            default=False,
        )
        parser.add_argument(
            '--rmuser',
            dest='rmuser',
            type=bool,
            default=False
        )

    def handle(self, *args, **options):
        if options['adduser']:
            self._adduser()
        elif options['rmuser']:
            self._rmuser()
