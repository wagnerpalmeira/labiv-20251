from django.shortcuts import render


promotions = [
    {
        'id': 1,
        'title': 'Promotion 1',
        'description': 'This is the first promotion',
    },
    {
        'id': 2,
        'title': 'Promotion 2',
        'description': 'This is the second promotion',
    }
]

def detail_promotion(request, promotion_id):
    context = {
        'promotion': promotions[int(promotion_id) - 1]
    }

    return render(request, 'promotions/detail_promotion.html',
                   context)
