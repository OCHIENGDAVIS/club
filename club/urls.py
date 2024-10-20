from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .contact import contact

urlpatterns = [
    path('cbv/', include('cbv.urls', namespace='cbv')),
    path('admin/', admin.site.urls),
    path('', include('events.urls', namespace='events')),
    path('contact-us/', contact, name='contact_us'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
