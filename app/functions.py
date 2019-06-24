import pandas as pd
import pickle
from nltk import word_tokenize
import csv
import random
import numpy as np
from .table import DrinkRateTable, MostPopularDrinksTable
from .models import DrinkRate, MostPopularDrinks

def get_ingredients_list():

    with open('assets/lists/alcoholic_list.csv', 'r') as f:
        reader = csv.reader(f)
        alcoholic_ingredients_list = list(reader)

    with open('assets/lists/non-alcoholic_list.csv', 'r') as f:
        reader = csv.reader(f)
        non_alcoholic_ingredients_list = list(reader)

    with open('assets/lists/fruit_list.csv', 'r') as f:
        reader = csv.reader(f)
        fruits_ingredients_list = list(reader)

    with open('assets/lists/other_list.csv', 'r') as f:
        reader = csv.reader(f)
        other_ingredients_list = list(reader)

    with open('assets/lists/glass_type_list.csv', 'r') as f:
        reader = csv.reader(f)
        glass_ingredients_list = list(reader)

    return zip(alcoholic_ingredients_list,non_alcoholic_ingredients_list,fruits_ingredients_list,other_ingredients_list,glass_ingredients_list)


def prepare_ingredients_list(request):

    ingredient_list = []

    for elementId, ingredient in request.POST.items():
        ingredient_list.append(str(ingredient))

    if len(ingredient_list) != 0:
        ingredient_list.pop(0)

    return ingredient_list


def find_in_vocab(ingredient_list):
    string = ''
    sset = []
    output = []
    ingredients = []
    for elem in ingredient_list:
        elem2 = word_tokenize(elem.lower())
        for part in elem2:
            ingredients.append(part)

    data_file = pd.read_csv('assets/ml_model/model_vocab.csv')
    ser = list(pd.Series(data_file['elem']))

    for elem in ingredients:
        if elem in ser:
            output.append(elem)

    for i in ingredients:
        for j in ingredients:
            string = i + '_' + j
            sset.append(string)
            string = ''

    sset = list(set(sset))
    slist = ['creme_de', 'grand_marnier', 'chambord_raspberry', 'midori_melon', 'malibu_rum',
             '151_proof', 'vanilla_ice-cream', 'dark_rum', 'jack_daniels', 'triple_sec',
             'sweet_and', 'blue_curacao', 'sour_mix', 'kahlua_baileys', 'irish_cream', 'absolut_citron',
             'peach_schnapps', 'ginger_ale', 'southern_comfort', 'maraschino_cherry', 'baileys_irish',
             'sweet_vermouth', 'egg_white', 'heavy_cream', 'dry_vermouth', 'club_soda', 'apricot_brandy',
             'sloe_gin', 'blended_whiskey', 'food_coloring', 'whipped_cream', 'red_wine', 'chocolate_syrop',
             'powdered_sugar', 'cocoa_powder', 'vanilla_extract', 'lemon-lime_soda']

    for elem in sset:
        if elem in slist:
            output.append(elem)

    return output


def get_deduced_ingredients(ingredient_list):
    ingredients = find_in_vocab(ingredient_list)

    if not ingredients:
        ingri = random.sample(['rum', 'vodka', 'gin', 'tequila', 'whiskey'], 2)
        drink = random.sample(['Rum Coca-cola', 'Vodka Coca-cola', 'Gin Tonic', 'Whiskey Coca-cola'], 2)

        return dict(ingredient1=ingri[0], ingredient2=ingri[1], drink1_name='Our proposition 1',
                    drink1=drink[0], drink2_name='Our proposition 2', drink2=drink[1])

    with open("assets/ml_model/model", 'rb') as file:
        model = pickle.load(file)

    results = model.most_similar(positive=ingredients)
    ingredients.append(results[0])
    ingredients.append(results[1])

    data_file1 = pd.read_csv("assets/ml_model/list.csv")
    counting_efects = np.zeros(len(data_file1.index))

    for index, row in data_file1.iterrows():
        for item in row:
            if item in ingredients:
                counting_efects[index] += 1
    max_elem = np.amax(counting_efects)

    indexes = []
    for i, elem in enumerate(counting_efects):
        if elem == max_elem:
            indexes.append(i)

    data_file2 = pd.read_csv('assets/ml_model/all_drinks.csv')
    data_file3 = pd.read_csv('assets/ml_model/csv_file.csv')
    ser2 = pd.Series(data_file2['strDrink'])
    ser3 = pd.Series(data_file3['list of ingedients'])

    if len(indexes) == 1:
        output = dict(ingredient1=(results[0])[0], ingredient2=(results[1])[0], drink1_name=ser2[indexes[0]],
                      drink1=ser3[indexes[0]].title(), drink2_name='Cuba Libre', drink2='Rum Coca-cola Lime Ice')
    else:
        found_indx = random.sample(indexes, 2)
        output = dict(ingredient1=(results[0])[0], ingredient2=(results[1])[0], drink1_name=ser2[found_indx[0]],
                      drink1=ser3[indexes[0]].title(), drink2_name=ser2[found_indx[1]], drink2=ser3[indexes[1]].title())

    return output


def add_drink_rate(c_user, c_drink_name, c_rate):
    if DrinkRate.objects.all().filter(user = c_user, drink_name = c_drink_name, rate = c_rate).exists():
        return None

    drink_rate = DrinkRate.create(c_user, c_drink_name, c_rate)
    drink_rate.save()

    if MostPopularDrinks.objects.all().filter(drink_name = c_drink_name).exists():
        drink_statictics = MostPopularDrinks.objects.get(drink_name = c_drink_name)
        drink_statictics.update(c_rate)
        drink_statictics.save()
    else:
        drink_statictics = MostPopularDrinks.create(c_drink_name, c_rate)
        drink_statictics.save()  


def get_higest_rated_drinks():
    table = MostPopularDrinksTable(MostPopularDrinks.objects.all().order_by('-rate_count','-rate_avarage',))
    return table    


def get_drink_rates_per_user(c_user):
    table = DrinkRateTable(DrinkRate.objects.filter( user = c_user).order_by('-rate'))
    return table


def get_drink_rate(c_drink_name):
    if MostPopularDrinks.objects.all().filter(drink_name = c_drink_name).exists():
        return MostPopularDrinks.objects.get(drink_name = c_drink_name).rate_avarage
    else:
        return 'not rated'

