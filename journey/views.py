from django.shortcuts import render, redirect
from  django.http import HttpResponse, JsonResponse
from . models import Place, ImagePlace

# Create your views here.


def index(request):
    places = Place.objects.all()
    context = {'places': places}
    return render(request, 'journey/index.html', context)


def image_detail(request, image_id):
    image = ImagePlace.objects.get(id=image_id)
    return redirect(image.get_absolute_url())


def get_place(request, slug):
    place = Place.objects.get(slug=slug)
    images = ImagePlace.objects.filter(place=place)
    data = {
        "title": f"{place.title}",
        "imgs": [ image.get_absolute_url() for image in images ],
        "description_short": f"{place.description_short}",
        "description_long": f"{place.description}",
        "coordinates": {
            "lng": f"{place.lng}",
            "lat": f"{place.lat}",
        }
    }
    return JsonResponse(data)


def get_markers(request,):
    places = Place.objects.all()
    markers = [{
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
          },
          "properties": {
            "title": f"{place.market_label}",
            "placeId": f"{place.place_id}",
            "detailsUrl": "{% url 'journey:get_place' " + "'" + place.slug + "'" +" %}"
          }
        } for place in places]
    return JsonResponse(markers)
