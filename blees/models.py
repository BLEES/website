from django.db import models


class Room(models.Model):
    """Represents a room"""
    room_name = models.CharField(max_length=30)

    def __str__(self):
        return "Room: %s" % self.room_name


class Measurement(models.Model):
    """Represents a given measurement"""
    room = models.ForeignKey(Room)
    taken = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    light = models.FloatField()

    def __str__(self):
        ret_str = ""
        ret_str += self.taken
        ret_str += (" Room %s: " % self.room)
        ret_str += ("temp: %s, " % self.temperature)
        ret_str += ("humidity: %s ," % self.humidity)
        ret_str += ("pressure: %s ," % self.pressure)
        ret_str += ("light: %s" % self.light)
        return "%s Room %s: temp: %s, humidity: %s, pressure: %s, light %s"