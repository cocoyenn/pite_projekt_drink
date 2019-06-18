import pickle
from nltk import word_tokenize
import csv
import random
import pandas as pd
import numpy as np
from gensim.models import Word2Vec


def get_ingredients_list():

    with open('assets/lists/alcoholic_list.txt', 'r') as f:
        reader = csv.reader(f)
        alcoholic_ingredients_list = list(reader)

    with open('assets/lists/non-alcoholic_list.txt', 'r') as f:
        reader = csv.reader(f)
        non_alcoholic_ingredients_list = list(reader)

    with open('assets/lists/fruit_list.txt', 'r') as f:
        reader = csv.reader(f)
        fruits_ingredients_list = list(reader)

    with open('assets/lists/other_list.txt', 'r') as f:
        reader = csv.reader(f)
        other_ingredients_list = list(reader)

    with open('assets/lists/glass_type_list.txt', 'r') as f:
        reader = csv.reader(f)
        glass_ingredients_list = list(reader)

    return zip(alcoholic_ingredients_list,non_alcoholic_ingredients_list,fruits_ingredients_list,other_ingredients_list,glass_ingredients_list)


def prepare_ingredients_list(request):

    ingredient_list = []

    for elementId, ingredient in request.POST.items():
        ingredient_list.append(str(ingredient))

    ingredient_list.pop(0)

    print(ingredient_list)

    return ingredient_list


def find_in_vocab(ingredient_list):
    
    string      = ''
    sset        = []
    output      = []
    ingredients = []
    for elem in ingredient_list:
        elem2 = word_tokenize(elem.lower())
        for part in elem2:
            ingredients.append(part)
    
    data_file = pd.read_csv('ml_model/model_vocab.csv')
    ser       = list(pd.Series(data_file['elem']))
        
    for elem in ingredients:
        if elem in ser:
            output.append(elem)
    
    for i in range(0, len(ingredients)):
        for j in range(i + 1, len(ingredients)):
            string = ingredients[i] + '_' + ingredients[j]
            sset.append(string)
            string = ''
    
    sset  = list(set(sset))
    slist = ['creme_de','grand_marnier','chambord_raspberry','midori_melon','malibu_rum',
            '151_proof','vanilla_ice-cream','dark_rum','jack_daniels','triple_sec',
            'sweet_and','blue_curacao','sour_mix','kahlua_baileys','irish_cream','absolut_citron',
            'peach_schnapps','ginger_ale','southern_comfort','maraschino_cherry','baileys_irish',
            'sweet_vermouth','egg_white','heavy_cream','dry_vermouth','club_soda','apricot_brandy',
            'sloe_gin','blended_whiskey','food_coloring','whipped_cream','red_wine','chocolate_syrop',
            'powdered_sugar','cocoa_powder','vanilla_extract','lemon-lime_soda']
    
    for elem in sset:
        if elem in slist:
            output.append(elem)
    
    
    return output


def generate_drinks(ingredient_list):
    
    ingredients = find_in_vocab(ingredient_list)
    
    if not ingredients:
        ingri = random.sample(['rum','vodka','gin','tequila','whiskey'],2)
        drink = random.sample(['Rum Coca-cola','Vodka Coca-cola','Gin Tonic','Whiskey Coca-cola'],2)
        
        return dict(ingredient1=ingri[0], ingredient2=ingri[1], drink1_name='Our proposition 1',
                    drink1=drink[0], drink2_name='Our proposition 2', drink2=drink[1])
    
    with open("ml_model/model", 'rb') as file:
        model = pickle.load(file)
    
    results = model.most_similar(positive = ingredients)
    ingredients.append(results[0])
    ingredients.append(results[1])
    
    data_file1      = pd.read_csv("ml_model/list.csv")
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
    
    data_file2 = pd.read_csv('ml_model/all_drinks.csv')
    data_file3 = pd.read_csv('ml_model/csv_file.csv')
    ser2 = pd.Series(data_file2['strDrink'])
    ser3 = pd.Series(data_file3['list of ingedients'])
    
    if len(indexes) == 1:
        output = dict(ingredient1=(results[0])[0].replace('_',' '), ingredient2=(results[1])[0].replace('_',' '), drink1_name=ser2[indexes[0]],
                    drink1=ser3[indexes[0]].title(), drink2_name='Cuba Libre', drink2='Rum Coca-cola Lime Ice')
    else:
        found_indx = random.sample(indexes, 2)
        output = dict(ingredient1=(results[0])[0].replace('_',' '), ingredient2=(results[1])[0].replace('_',' '), drink1_name=ser2[found_indx[0]],
                    drink1=ser3[indexes[0]].title(), drink2_name=ser2[found_indx[1]], drink2=ser3[indexes[1]].title())
    
    return output