from django.shortcuts import render
from promotions.models import Promotion

def home_view(request):
    promotions = Promotion.objects.all().select_related('category')
    context = {
        'promotions': promotions
    }
    return render(request, 'home/home.html', context)
