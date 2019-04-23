from django.contrib import admin

# Register your models here.
from reminder.models import Reminder, RadioStation, Category, Guest, Host, ShowHost, Tag, Show
from user.models import Listener

admin.site.register(Reminder)
admin.site.register(RadioStation)
admin.site.register(Category)
admin.site.register(Guest)
admin.site.register(Host)
admin.site.register(ShowHost)
admin.site.register(Tag)
admin.site.register(Listener)
admin.site.register(Show)