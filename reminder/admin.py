from django.contrib import admin
from reminder.models import Reminder, RadioStation, Category, Guest, Host, ShowHost, Tag, Show
# Register your models here.

admin.site.register(Reminder)
admin.site.register(RadioStation)
admin.site.register(Category)
admin.site.register(Guest)
admin.site.register(Host)
admin.site.register(ShowHost)
admin.site.register(Tag)
admin.site.register(Show)