from django.shortcuts import render

posts = [ 
    {
        'title': 'Nasza apka'
    }
]

def home(request):
    context = { 
        'posts': posts
    }
    return render(request, 'dd_app/home.html', context)

def about(request):
    return render(request, 'dd_app/about.html', context)