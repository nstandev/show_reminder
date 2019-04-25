from django import forms
from reminder.models import Reminder


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ('time', 'show')


