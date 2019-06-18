import pandas as pd
import pickle
from nltk import word_tokenize
import csv
import random
import numpy as np


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

    if ('creme' in ingredients) and ('de' in ingredients):
        output.append('creme_de')

    if ('grand' in ingredients) and ('marnier' in ingredients):
        output.append('grand_marnier')

    if ('chambord' in ingredients) and ('raspberry' in ingredients):
        output.append('chambord_raspberry')

    if ('midori' in ingredients) and ('melon' in ingredients):
        output.append('midori_melon')

    if ('malibu' in ingredients) and ('rum' in ingredients):
        output.append('malibu_rum')

    if ('151' in ingredients) and ('proof' in ingredients):
        output.append('151_proof')

    if ('vanilla' in ingredients) and ('ice-cream' in ingredients):
        output.append('vanilla_ice-cream')

    if ('dark' in ingredients) and ('rum' in ingredients):
        output.append('dark_rum')

    if ('jack' in ingredients) and ('daniels' in ingredients):
        output.append('jack_daniels')

    if ('triple' in ingredients) and ('sec' in ingredients):
        output.append('triple_sec')

    if ('sweet' in ingredients) and ('and' in ingredients):
        output.append('sweet_and')

    if ('blue' in ingredients) and ('curacao' in ingredients):
        output.append('blue_curacao')

    if ('sour' in ingredients) and ('mix' in ingredients):
        output.append('sour_mix')

    if ('kahlua' in ingredients) and ('baileys' in ingredients):
        output.append('kahlua_baileys')

    if ('irish' in ingredients) and ('cream' in ingredients):
        output.append('irish_cream')

    if ('absolut' in ingredients) and ('citron' in ingredients):
        output.append('absolut_citron')

    if ('peach' in ingredients) and ('schnapps' in ingredients):
        output.append('peach_schnapps')

    if ('ginger' in ingredients) and ('ale' in ingredients):
        output.append('ginger_ale')

    if ('southern' in ingredients) and ('comfort' in ingredients):
        output.append('southern_comfort')

    if ('maraschino' in ingredients) and ('cherry' in ingredients):
        output.append('maraschino_cherry')

    if ('baileys' in ingredients) and ('irish' in ingredients):
        output.append('baileys_irish')

    if ('sweet' in ingredients) and ('vermouth' in ingredients):
        output.append('sweet_vermouth')

    if ('egg' in ingredients) and ('white' in ingredients):
        output.append('egg_white')

    if ('heavy' in ingredients) and ('cream' in ingredients):
        output.append('heavy_cream')

    if ('dry' in ingredients) and ('vermouth' in ingredients):
        output.append('dry_vermouth')

    if ('club' in ingredients) and ('soda' in ingredients):
        output.append('club_soda')

    if ('apricot' in ingredients) and ('brandy' in ingredients):
        output.append('apricot_brandy')

    if ('sloe' in ingredients) and ('gin' in ingredients):
        output.append('sloe_gin')

    if ('blended' in ingredients) and ('whiskey' in ingredients):
        output.append('blended_whiskey')

    if ('food' in ingredients) and ('coloring' in ingredients):
        output.append('food_coloring')

    if ('whipped' in ingredients) and ('cream' in ingredients):
        output.append('whipped_cream')

    if ('red' in ingredients) and ('wine' in ingredients):
        output.append('red_wine')

    if ('chocolate' in ingredients) and ('syrop' in ingredients):
        output.append('chocolate_syrop')

    if ('powdered' in ingredients) and ('sugar' in ingredients):
        output.append('powdered_sugar')

    if ('cocoa' in ingredients) and ('powder' in ingredients):
        output.append('cocoa_powder')

    if ('vanilla' in ingredients) and ('extract' in ingredients):
        output.append('vanilla_extract')

    if ('lemon-lime' in ingredients) and ('soda' in ingredients):
        output.append('lemon-lime_soda')

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