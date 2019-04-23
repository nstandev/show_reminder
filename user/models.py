from django.db import models

# Create your models here.


class Listener(models.Model):
    email = models.EmailField(max_length=70, blank=True)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username

