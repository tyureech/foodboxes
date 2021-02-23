from django.core.management.base import BaseCommand
import script


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        if options['full']:
            script.create_data_reviews('https://raw.githubusercontent.com/stepik-a-w'
                                       '/drf-project-boxes/master/reviews.json')
            script.create_data_user("https://raw.githubusercontent.com/"
                                    "stepik-a-w/drf-project-boxes/master/recipients.json")
            script.create_data_item('https://raw.githubusercontent.com/stepik-a-w'
                                    '/drf-project-boxes/master/foodboxes.json')
        elif options['items']:
            script.create_data_item('https://raw.githubusercontent.com/stepik-a-w'
                                    '/drf-project-boxes/master/foodboxes.json')
        elif options['users']:
            script.create_data_user("https://raw.githubusercontent.com/"
                                    "stepik-a-w/drf-project-boxes/master/recipients.json")
        elif options['reviews']:
            script.create_data_reviews('https://raw.githubusercontent.com/stepik-a-w'
                                       '/drf-project-boxes/master/reviews.json')



    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--full',
            action='store_true',
            default=False,
            help='Создать и обновить все записи во всех базах данных'
        )
        parser.add_argument(
            '--items',
            action='store_true',
            default=False,
            help='Создать или обновить записи в базе данных items'
        )
        parser.add_argument(
            '--users',
            action='store_true',
            default=False,
            help='Создать или обновить записи в базе данных users'
        )
        parser.add_argument(
            '--reviews',
            action='store_true',
            default=False,
            help='Создать или обновить записи в базе данных reviews'
        )
