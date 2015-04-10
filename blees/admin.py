from django.contrib import admin
from blees.models import Room, Measurement


class RoomAdmin(admin.ModelAdmin):
    pass
admin.site.register(Room, RoomAdmin)


class MeasurementAdmin(admin.ModelAdmin):
    pass
admin.site.register(Measurement, MeasurementAdmin)
