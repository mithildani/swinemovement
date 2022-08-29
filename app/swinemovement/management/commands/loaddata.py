from django.core.management import BaseCommand
from swinemovement.scripts.load_dummy_data import load_dummy_data


class Command(BaseCommand):
    """
        python manage.py loaddata
    """

    def add_arguments(self, parser):
        #parser.add_argument('--image-tag', required=False, type=str, default=None)
        pass

    def handle(self, *args, **kwargs):
        load_dummy_data()
