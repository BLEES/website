from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.decorators.cache import cache_page
from django.utils.encoding import force_text
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

from blees.models import Room, Measurement


# @cache_page(60 * 2)  # cache for 2 minutes
def index(request):
    rooms = list(Room.objects.all())
    template = loader.get_template('blees/index.html')
    context = RequestContext(request, {
        'rooms': rooms,
    })
    return HttpResponse(template.render(context))


def room_last_week(request, room_name):
    try:
        Room.objects.get(room_name=room_name)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    template = loader.get_template('blees/last_week_graphs.html')
    context = RequestContext(request, {
        'room_name': room_name,
    })
    return HttpResponse(template.render(context))


@csrf_exempt
def add_measurement(request, room):
    room_obj = get_object_or_404(Room, room_name=room)
    temp = float(request.POST['temp'])
    humidity = float(request.POST['humidity'])
    pressure = float(request.POST['pressure'])
    light = float(request.POST['light'])
    new_measurement = Measurement(room=room_obj, temperature=temp,
                                  pressure=pressure, humidity=humidity,
                                  light=light)

    new_measurement.save()

    return HttpResponseRedirect(reverse('index'))
