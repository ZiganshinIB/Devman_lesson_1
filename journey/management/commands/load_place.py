from django.core.management.base import BaseCommand
from django.core.files import File
from django.utils.text import slugify

import requests
import json
from io import BytesIO


from journey.models import Place, ImagePlace


class Command(BaseCommand):
    help = 'Load places from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='Path to JSON file with places')

    def load_places(self, url):
        response = requests.get(url)
        place_json = json.loads(response.content)
        place = Place()
        place.title = place_json['title']
        place.place_id = slugify(place_json['title'])
        place.description = place_json['description_long']
        place.description_short = place_json['description_short']
        place.lat = place_json['coordinates']['lat']
        place.lng = place_json['coordinates']['lng']
        place.save()
        for img in place_json['imgs']:
            p = requests.get(img)
            title = img.split('/')[-1]
            buf = BytesIO()
            buf.write(p.content)
            image = ImagePlace()
            image.image = File(buf, name=title)
            image.place = place
            image.save()

    def handle(self, *args, **options):
        url = options['url']
        self.load_places(url)
