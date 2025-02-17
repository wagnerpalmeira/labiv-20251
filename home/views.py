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

def home_view(request):
    context = {
        'promotions': promotions
    }
    return render(request, 'home/home.html', context)
