from django.urls import path

from reminder import views

app_name = 'reminder'

urlpatterns = [
    path('', views.index),

]