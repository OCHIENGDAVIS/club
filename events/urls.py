from django.urls import path

from . import views
from comments.views import CommentCreate

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.all_events, name='all_events'),
    path('event/<int:id>/', views.event_detail, name='detail'),
    path('event/<int:id>/comments/create/', CommentCreate.as_view(), name='comments_create'),
    path('event/<int:id>/add-venue/', views.add_venue, name='add_venue'),
    path('event/gentext/', views.get_text, name='generate_text_file'),
    path('event/gencsv', views.gen_csv, name='generate_csv'),
    path('event/genpdf', views.gen_pdf, name='generate_pdf'),
    path('event/context-demo/', views.context_demo, name='context_demo'),
    path('event/committee/', views.committee_formset, name='committee'),
    path('events/survey/', views.SurveyWizard.as_view(), name='survey'),

]
