from django.db import models


class Room(models.Model):
    """Represents a room"""
    room_name = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % self.room_name


class Measurement(models.Model):
    """Represents a given measurement"""
    room = models.ForeignKey(Room)
    taken = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    light = models.FloatField()

    def __str__(self):
        ret_str = ""
        ret_str += self.taken.strftime("%x %X")
        ret_str += (" | Room {0}".format(self.room))
        # ret_str += ("temp: {0}, ".format(self.temperature))
        # ret_str += ("humidity: {0}, ".format(self.humidity))
        # ret_str += ("pressure: {0}, ".format(self.pressure))
        # ret_str += ("light: {0}".format(self.light))
        return ret_str

