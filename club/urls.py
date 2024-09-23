from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .contact import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls', namespace='events')),
    path('contact-us/', contact, name='contact_us'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
