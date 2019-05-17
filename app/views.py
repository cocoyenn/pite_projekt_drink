from django.shortcuts import render

settings = {
    'app_name': 'Drink Advisor',
}

app_name = 'Drink Advisor'


def home(request):
    context = {
        'settings': settings,
        'title': 'Home',
        'app_name': app_name
    }
    return render(request, 'app/home.html', context)


def about(request):
    context = {
        'settings': settings,
        'title': 'About',
        'app_name': app_name
    }
    return render(request, 'app/about.html', context)
