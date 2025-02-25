from django.contrib import admin
from django.urls import path, include
from home.views import home_view
from promotions.views import detail_promotion

urlpatterns = [
    path('', home_view),
    path('promotions/', include('promotions.urls')),
    path('admin/', admin.site.urls),
]
