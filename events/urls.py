from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.all_events, name='all_events'),
    path('event/<int:id>/', views.event_detail, name='detail'),
    path('event/<int:id>/add-venue/', views.add_venue, name='add_venue'),
    path('event/gentext/', views.get_text, name='generate_text_file'),
    path('event/gencsv', views.gen_csv, name='generate_csv'),

]
