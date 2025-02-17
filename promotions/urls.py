from django.urls import path
from promotions.views import detail_promotion

urlpatterns = [
    path('<int:promotion_id>/',
          detail_promotion),
]
