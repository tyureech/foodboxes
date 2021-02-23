import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'foodboxes.settings'
django.setup()


from django.utils.dateparse import parse_datetime
import pytz
import requests

from items.models import Items
from reviews.models import Reviews
from users.models import User


def create_data_item(http_address):
    print('OK')
    response = requests.get(http_address).json()
    for item in response:
        data_items = Items(
            id=item['id'],
            title=item['title'],
            description=item['description'],
            image=item['image'],
            weight=item['weight_grams'],
            price=item['price'],
        )
        data_items.save()


def create_data_user(http_address):
    print('OK')
    response = requests.get(http_address).json()
    for item in response:
        data_users = User(
            id=item['id'],
            email=item['email'],
            username=item['email'].split('@')[0],
            password=item['password'],
            first_name=item['info']['name'],
            last_name=item['info']['surname'],
            middle_name=item['info']['patronymic'],
            phone=item['contacts']['phoneNumber'],
            address="item['city_kladr']",
        )
        data_users.save()


def create_data_reviews(http_address):
    print('OK')
    response = requests.get(http_address).json()
    for item in response:
        data_review = Reviews(
            id=item['id'],
            author=User.objects.get(id=item['id']),
            text=item['content'],
            created_at=pytz.timezone("Europe/Moscow").localize(parse_datetime(item['created_at'] + ' 00:00:00')),
            published_at=pytz.timezone("Europe/Moscow").localize(parse_datetime(
                item['published_at'] + ' 00:00:00' if item['published_at'] != '' else '1111-11-11 11:11:11')        # Временное решение
            ),
            status=item['status'],
        )
        data_review.save()


if __name__ == '__main__':
    create_data_item('https://raw.githubusercontent.com/stepik-a-w'
                            '/drf-project-boxes/master/foodboxes.json')
    create_data_user("https://raw.githubusercontent.com/"
                            "stepik-a-w/drf-project-boxes/master/recipients.json")
    create_data_reviews('https://raw.githubusercontent.com/stepik-a-w'
                        '/drf-project-boxes/master/reviews.json')
