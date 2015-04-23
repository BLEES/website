from datetime import datetime, timedelta

from django import template
from django.template.loader import get_template

from blees import models

register = template.Library()


@register.inclusion_tag('blees/vis_header.html')
def vis_header(m_class):
    room = models.Room.objects.filter(room_name=m_class)
    weeks_measurements = models.Measurement.objects.filter(room=room, taken__gte=datetime.today() - timedelta(weeks=1))
    weeks_measurements = weeks_measurements.order_by('taken')
    measurements = list(weeks_measurements)

    # Note that this is hacked to get the timezone correct, should change in future
    temps = [(o.taken - timedelta(hours=4), o.temperature) for o in measurements]
    """:type : list[float]"""
    humidities = [(o.taken - timedelta(hours=4), o.humidity) for o in measurements]
    """:type : list[float]"""
    pressures = [(o.taken - timedelta(hours=4), o.pressure) for o in measurements]
    """:type : list[float]"""
    lights = [(o.taken - timedelta(hours=4), o.light) for o in measurements]
    """:type : list[float]"""

    return {
        'temps': temps,
        'humidities': humidities,
        'pressures': pressures,
        'lights': lights,
        'room_n': room[:1].get().room_name,
    }