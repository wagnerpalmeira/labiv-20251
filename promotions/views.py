from django.shortcuts import render
from .models import Promotion
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import PromotionForm
from django.views.generic import DetailView

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'promotions/detail_promotion.html'
    context_object_name = 'promotion'
    pk_url_kwarg = 'promotion_id'


# def detail_promotion(request, promotion_id):
#     promotion = get_object_or_404(Promotion, id=promotion_id)

#     return render(request, 'promotions/detail_promotion.html',
#                    {'promotion': promotion})

@login_required
def create_promotion(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST, request.FILES)
        if form.is_valid():
            promotion = form.save(commit=False)
            # promotion.user = request.user
            promotion.save()
            return redirect('home')
        
    else:
        form = PromotionForm()

    return render(request, 'promotions/create_promotion.html', 
                  {'form': form})
