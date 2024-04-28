from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

import requests

from journey.models import Place, ImagePlace


def load_place(url):
    response = requests.get(url)
    response.raise_for_status()
    raw_place = response.json()
    if 'error' in raw_place:
        raise requests.exceptions.HTTPError(raw_place['error'])

    place, created = Place.objects.update_or_create(
        title=raw_place['title'],
        defaults={
            'long_description': raw_place['description_long'],
            'short_description': raw_place['description_short'],
            'lat': raw_place['coordinates']['lat'],
            'lng': raw_place['coordinates']['lng'],
        }
    )
    for url_image in raw_place['imgs']:
        raw_image = requests.get(url_image)
        raw_image.raise_for_status()
        ImagePlace.objects.create(image=ContentFile(raw_image.content, name=url_image.split('/')[-1]), place=place)


class Command(BaseCommand):
    help = 'Load places from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='Path to JSON file with places')

    def handle(self, *args, **options):
        url = options['url']
        try:
            load_place(url)
        except MultipleObjectsReturned:
            print('Places with such fields more than 1 in the Database')
