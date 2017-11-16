from contextlib import contextmanager

from django.core.management.base import BaseCommand, CommandError

from apps.accounts.factories import UserFactory
from apps.accounts.models import User
from apps.costcontrol.factories import BalanceRecordFactory, SpendingCategoryFactory

EMAIL = 'test@example.com'


@contextmanager
def command_error_context():
    try:
        yield
    except Exception as error:
        raise CommandError(error)


class Command(BaseCommand):
    help = 'Preparing for cypress tests.'

    def _init(self):
        user = UserFactory.build(email=EMAIL)
        user.set_password('password123')
        with command_error_context():
            user.save()
            spending = SpendingCategoryFactory(user=user)
            BalanceRecordFactory(category=spending)

    def _destroy(self):
        with command_error_context():
            User.objects.get(email=EMAIL).delete()

    def add_arguments(self, parser):
        parser.add_argument(
            '--init',
            dest='init',
            type=bool,
            default=False,
        )
        parser.add_argument(
            '--destroy',
            dest='destroy',
            type=bool,
            default=False
        )

    def handle(self, *args, **options):
        if options['init']:
            self._init()
        elif options['destroy']:
            self._destroy()
