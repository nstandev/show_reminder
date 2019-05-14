from django.urls import path

from reminder import views

app_name = 'reminder'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-reminder', views.add_reminder, name='add_reminder'),
    path('add-show', views.add_show, name='add_show'),
    path('add-cat', views.add_cat, name='add_cat'),
    path('add-radio-station', views.add_radio, name='add_radio_staion'),
    path('add-guest', views.add_guest, name='add_guest'),
    # path('add-reminder', views.add_reminder, name='add_reminder'),

]