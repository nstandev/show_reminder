from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from reminder.models import Reminder


def index(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminder/index.html', {'reminders': reminders})