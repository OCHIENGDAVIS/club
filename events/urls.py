from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.all_events, name='all_events'),
    path('event/<int:id>/', views.event_detail, name='detail'),
]
