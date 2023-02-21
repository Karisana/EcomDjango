from django.urls import path, include
from django.conf.urls.static import static

from .views import *

app_name = 'store'

urlpatterns = [
    path('', all_products, name='home')
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
