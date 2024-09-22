from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<str:month>/', views.index, name='list_by_year_month'),
]
