from django.contrib import admin
from django.urls import path, include
from home.views import home_view
from promotions.views import detail_promotion
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view),
    path('promotions/', include('promotions.urls')),
    path('admin/', admin.site.urls),
]+ debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT)
