from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy

from . models import Place, ImagePlace


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
            "placeId": f"{place.place_id}",
            "detailsUrl": reverse("journey:get_place", kwargs={"pk": place.pk}),
        }
    } for place in places]
    Geo_JSON = {"type": "FeatureCollection", "features": markers}
    context = {
        "geojson": Geo_JSON
    }
    return render(request, 'journey/index.html', context)


def get_place(request, pk):
    place = Place.objects.get(pk=pk)
    images = ImagePlace.objects.filter(place=place)
    data = {
        "title": f"{place.title}",
        "imgs": [image.image.url for image in images],
        "description_short": f"{place.short_description}",
        "description_long": f"{place.long_description}",
        "coordinates": {
            "lng": f"{place.lng}",
            "lat": f"{place.lat}",
        }
    }
    return JsonResponse(data)


def place(request, pk):
    place = get_object_or_404(Place, pk=pk)
    data = {
        "title": f"{place.title}",
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": f"{place.short_description}",
        "description_long": f"{place.long_description}",
        "coordinates": {
            "lng": f"{place.lng}",
            "lat": f"{place.lat}",
        }
    }
    return JsonResponse(data, safe=True, json_dumps_params={'ensure_ascii': False, 'indent': 2})


def handle404(request, exception):
    return render(request, '404.html', status=404)
