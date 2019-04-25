from django.urls import path

from reminder import views

app_name = 'reminder'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-reminder', views.add_reminder, name='add_reminder'),
    path('add-reminder', views.add_reminder, name='add_reminder'),

]