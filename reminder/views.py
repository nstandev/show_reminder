from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from reminder.forms import ReminderForm, ShowForm, CatForm, GuestForm, RadioStationForm
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


def add_show(request):
    if request.method != 'POST':
        form = ShowForm()
    else:
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            next = request.POST.get('next', '/add-reminder')

            return HttpResponseRedirect(next)
        else:
            return HttpResponse('Form is Not Valid')

    context = {'form': form}
    return render(request, 'reminder/add-show.html', context)


def add_cat(request):
    if request.method != 'POST':
        form = CatForm()
    else:
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'reminder/add-cat.html', context)


def add_radio(request):
    if request.method != 'POST':
        form = RadioStationForm()
    else:
        form = RadioStationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'reminder/add-radio-station.html', context)


def add_guest(request):
    if request.method != 'POST':
        form = GuestForm()
    else:
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'reminder/add-guest.html', context)


