from django.conf.urls import include, url
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	# admin/
    url(r'^admin/', admin.site.urls),

    # accounts/
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    # dashboard/
    url(r'dashboard/', include('dashboard.urls', namespace='dashboard')),

    # events/
    url(r'events/', include('events.urls', namespace='events')),

   	# Redirect all other urls
    url(r'^.*$', RedirectView.as_view(url=reverse_lazy('dashboard:index'))),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)