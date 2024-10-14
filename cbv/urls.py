from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from . import views

app_name = 'cbv'

urlpatterns = [
    path('', views.TemplateViewDemo.as_view(), name='index'),
    path('redirect/', RedirectView.as_view(pattern_name='cbv:index')),
    path('events/', views.EventListView.as_view(), name='list'),
    path('event/<int:pk>/', views.EventDetail.as_view(), name='detail'),
    path('event/<int:pk>/update/', views.EventEditView.as_view(), name='update'),
    path('event/<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete'),
    path('event/create/', views.EventCreateView.as_view(), name='create'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
