from django.shortcuts import render
def index(request):
    context = {
        'home': 'home',
        'about': 'about',
        'contact': 'contact',
    }
    return render(request, 'home.html', context)