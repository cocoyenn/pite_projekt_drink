from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import csv


def home(request):
    context = {
        'title': 'Home',
        'app_name': settings.APP_NAME
    }

    ingredients = {
        'alkoholic': [],
        'non-alcoholic': [],
        'frutis': [],
        'other': [],
        'glass': []
    }

    with open('assets/lists/alcoholic_list.txt', 'r') as f:
        reader = csv.reader(f)
        ingredients['alkoholic'] = list(reader)

    with open('assets/lists/non-alcoholic_list.txt', 'r') as f:
        reader = csv.reader(f)
        ingredients['non-alkoholic'] = list(reader)

    with open('assets/lists/fruit_list.txt', 'r') as f:
        reader = csv.reader(f)
        ingredients['fruits'] = list(reader)

    with open('assets/lists/other_list.txt', 'r') as f:
        reader = csv.reader(f)
        ingredients['other'] = list(reader)

    with open('assets/lists/glass_type_list.txt', 'r') as f:
        reader = csv.reader(f)
        ingredients['glass'] = list(reader)

    return render(request, 'app/home.html', context, ingredients)


def about(request):
    context = {
        'title': 'About',
        'app_name': settings.APP_NAME
    }
    return render(request, 'app/about.html', context)


def makeDrink(request):
    ingredientList = []

    for elementId, ingredient in request.POST.items():
        ingredientList.append(str(ingredient))

    ingredientList.pop(0)
    print(ingredientList)

    ###
    # INSERT MACHINE LEARNING MAGIC HERE

    context = {
        'title': 'Drink maked!',
        'app_name': settings.APP_NAME,
    }
    return render(request, 'app/home.html', context)


def user_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {'settings': settings,
               'title': 'Login',
               'app_name': app_name,
               'user_form': user_form,
               'profile_form': profile_form,
               'registered': registered}
    return render(request, 'app/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('app-home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        context = {
            'settings': settings,
            'title': 'Login',
            'app_name': app_name
        }
        return render(request, 'app/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app-home'))
