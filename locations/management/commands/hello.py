from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Count loop'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument(
            '--count',
            type=int,
            default=1,
            help='Number of iterations (must be positive)'
        )

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        count = kwargs['count']

        # Validate input
        if count <= 0:
            raise CommandError('Count must be a positive integer')

        self.stdout.write(
            self.style.SUCCESS(f'Hi, {name}!')
        )

        for i in range(1, count + 1):
            self.stdout.write(f'Count {i}')