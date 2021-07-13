from django.db import models


class ICUModels(models.Model):
    icu_name = models.CharField(max_length=255)
    total_ventilator = models.IntegerField(default=0)
    ventilator_left = models.IntegerField(default=0)
    total_unventilator = models.IntegerField(default=0)
    unventilator_left = models.IntegerField(default=0)

    def __str__(self):
        return self.icu_name


class IsolationRoom(models.Model):
    room_name = models.CharField(max_length=255)
    total_bed = models.IntegerField(default=0)
    bed_left = models.IntegerField(default=0)

    def __str__(self):
        return self.room_name


class SpecialRoom(models.Model):
    s_name = models.CharField(max_length=255)
    total_ventilator = models.IntegerField(default=0)
    ventilator_left = models.IntegerField(default=0)

    def __str__(self):
        return self.s_name
