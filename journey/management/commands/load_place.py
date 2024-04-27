from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.core.files import File
from django.utils.text import slugify

import requests
import json
from io import BytesIO


from journey.models import Place, ImagePlace


def load_places(url):
    response = requests.get(url)
    place_json = json.loads(response.content)
    place, created = Place.objects.get_or_create(
        title=place_json['title'],
        long_description=place_json['description_long'],
        chort_description=place_json['description_short'],
        lat=place_json['coordinates']['lat'],
        lng=place_json['coordinates']['lng'],
    )
    for img in place_json['imgs']:
        p = requests.get(img)
        name = img.split('/')[-1]
        image = ImagePlace()
        image.place = place
        image.image.save(name, ContentFile(p.content))


class Command(BaseCommand):
    help = 'Load places from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='Path to JSON file with places')

    def handle(self, *args, **options):
        url = options['url']
        load_places(url)
