from django import forms
from django.forms import PasswordInput

from reminder.models import Reminder, Show, Category, Guest, RadioStation
from user.models import Listener


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ('time', 'show',)


class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('title', 'category', 'host', 'radio_station', 'schedule', 'tag',)


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'occupation', 'show',)


class RadioStationForm(forms.ModelForm):
    class Meta:
        model = RadioStation
        fields = ('name', 'location', 'freq')

