from django.db import models
from user.models import Listener

# Create your models here.


class RadioStation (models.Model):
    LOCATION_CHOICES = ()

    name = models.CharField(max_length=30)
    freq = models.CharField(max_length=30)
    location = models.CharField(max_length=30, choices=LOCATION_CHOICES)


class Tag(models.Model):
    name = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=30)


class Host (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    oap_name = models.CharField(max_length=30)
    radio_station = models.ForeignKey(RadioStation, on_delete=models.CASCADE)


class Show (models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    host = models.ManyToManyField(Host, through='ShowHost')
    schedule = models.DateField()
    radio_station = models.ForeignKey(RadioStation, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, through='ShowTag')


class ShowHost (models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)


class Guest (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)


class ShowTag(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Reminder(models.Model):
    listener = models.ForeignKey(Listener, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    time = models.DateField()


