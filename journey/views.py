from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place, ImagePlace


def index(request):
    places = Place.objects.all()
    markers = [{
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        },
        "properties": {
            "title": f"{place.title}",
            "placeId": f"{place.id}",
            "detailsUrl": reverse('journey:place', args=[place.id]),
        }
    } for place in places]
    geo_json = {"type": "FeatureCollection", "features": markers}
    context = {
        "geojson": geo_json
    }
    return render(request, 'journey/index.html', context)


def place(request, pk):
    images = Place.objects.get(id=pk).select_related('images')
    geo_data = {
        "title": f"{place.title}",
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": f"{place.short_description}",
        "description_long": f"{place.long_description}",
        "coordinates": {
            "lng": f"{place.lng}",
            "lat": f"{place.lat}",
        }
    }
    return JsonResponse(geo_data, safe=True, json_dumps_params={'ensure_ascii': False, 'indent': 2})

