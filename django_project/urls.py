from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from gallery.views import index

urlpatterns = [
    # path('', index, name='index'),
    path('', index, name='index'),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path('artworks/', include('artworks.urls')),
    path('events/', include('events.urls')),
    path('artists/', include('creators.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
