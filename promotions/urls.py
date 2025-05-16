from django.urls import path
from promotions.views import PromotionDetailView, create_promotion

app_name = 'promotions'

urlpatterns = [
    path('<int:promotion_id>/',
          PromotionDetailView.as_view(), name='detail_promotion'),
    path('create/', create_promotion, name='create_promotion'), 
]
