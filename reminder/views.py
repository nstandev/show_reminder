from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from reminder.forms import ReminderForm
from reminder.models import Reminder


def index(request):
    reminders = Reminder.objects.all()
    return render(request, 'reminder/index.html', {'reminders': reminders})


def add_reminder(request):
    if request.method != 'POST':
        form = ReminderForm()
    else:
        form = ReminderForm(request.POST)
        if form.is_valid():
            current_user = request.user

            form_obj = form.save(commit=False)
            form_obj.listener_id = current_user.id
            form_obj.save()

            return HttpResponseRedirect(reverse('reminder:index'))
        else:
            return HttpResponse('Form is Not Valid')

    context = {'form':form}
    return render(request, 'reminder/add-reminder.html', context)

