from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm , EditUserForm, EditUserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .table import DrinkRateTable
from .models import DrinkRate
from .functions import *


def home(request):
    table = DrinkRateTable(DrinkRate.objects.all())
    context = {
        'title': 'Home',
        'app_name': settings.APP_NAME,
        'ingredients': get_ingredients_list(),
        'table': table
    }
    return render(request, 'app/home.html', context)


def about(request):
    context = {
        'title': 'About',
        'app_name': settings.APP_NAME
    }
    return render(request, 'app/about.html', context)


def makeDrink(request):

    context = {
        'title': 'Drink maked!',
        'app_name': settings.APP_NAME,
        'ingredient_list': prepare_ingredients_list(request),
    }
    prepared_drinks = generate_drinks(context['ingredient_list'])

    return render(request, 'app/drinkReady.html', context, prepared_drinks)


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
               'app_name': settings.APP_NAME,
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
            context = {
            'settings': settings,
            'title': 'Login failed try again!',
            'app_name': settings.APP_NAME,
            'info':"Login failed try again!"
        }
        return render(request, 'app/login.html', context)
    else:
        context = {
            'settings': settings,
            'title': 'Login',
            'app_name': settings.APP_NAME
        }
        return render(request, 'app/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app-home'))


def profile_site(request):
    table = DrinkRateTable(DrinkRate.objects.all())

    context = {
       'settings': settings,
        'title': 'Profile site',
        'app_name': settings.APP_NAME,
        'info':"Profile site",
        'table': table        
    }
    return render(request, 'app/profile.html', context)

def profile_edition(request):
    edited = False
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = UserProfileInfoForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            request.user = user_form.save()
            request.user.save()
            request.profile = profile_form.save(commit=False)
            request.profile.user = request.user
            if 'profile_pic' in request.FILES:
                request.profile.profile_pic = request.FILES['profile_pic']
            request.profile.save()
            edited = True
            return HttpResponseRedirect(reverse('app-profile'))
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditUserProfileInfoForm(instance=request.user)
    context = {
        'settings': settings,
        'title': 'Edit',
        'app_name': settings.APP_NAME,
        'user_form': user_form,
        'profile_form': profile_form,
        'edited': edited
        }
    return render(request,'app/profile_edition.html', context)