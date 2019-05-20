from django.db import models
from account.models import User

# Create your models here.

STATE = (
    ("Abia", "Abia",),
    ("Adamawa", "Adamawa",),
    ("Anambra", "Anambra",),
    ("Akwa Ibom", "Akwa Ibom",),
    ("Bauchi", "Bauchi",),
    ("Bayelsa", "Bayelsa",),
    ("Benue", "Benue",),
    ("Borno", "Borno"),
    ("Cross River", "Cross River",),
    ("Delta", "Delta",),
    ("Ebonyi", "Ebonyi",),
    ("Enugu", "Enugu",),
    ("Edo", "Edo",),
    ("Ekiti", "Ekiti",),
    ("FCT - Abuja", "FCT - Abuja",),
    ("Gombe", "Gombe",),
    ("Imo", "Imo",),
    ("Jigawa", "Jigawa",),
    ("Kaduna", "Kaduna",),
    ("Kano", "Kano",),
    ("Katsina", "Katsina",),
    ("Kebbi", "Kebbi",),
    ("Kogi", "Kogi",),
    ("Kwara", "Kwara",),
    ("Lagos", "Lagos",),
    ("Nasarawa", "Nasarawa",),
    ("Niger", "Niger",),
    ("Ogun", "Ogun",),
    ("Ondo", "Ondo",),
    ("Osun", "Osun",),
    ("Oyo", "Oyo",),
    ("Plateau", "Plateau",),
    ("Rivers", "Rivers",),
    ("Sokoto", "Sokoto",),
    ("Taraba", "Taraba",),
    ("Yobe", "Yobe",),
    ("Zamfara", "Zamfara"),
)


class RadioStation (models.Model):
    name = models.CharField(max_length=30)
    freq = models.CharField(max_length=30)
    location = models.CharField(max_length=30, choices=STATE)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Host (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    oap_name = models.CharField(max_length=30)
    radio_station = models.ForeignKey(RadioStation, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Show (models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    host = models.ManyToManyField(Host, through='ShowHost')
    schedule = models.DateField()
    radio_station = models.ForeignKey(RadioStation, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, through='ShowTag')

    def __str__(self):
        return self.title


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
    listener = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    time = models.DateField()

    def __str__(self):
        return self.show.title + ' reminder'


