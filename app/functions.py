import csv
import pandas as pd
import pickle
from nltk import word_tokenize
import csv
import random
import numpy as np
from gensim.models import Word2Vec


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

    ingredient_list.pop(0)

    print(ingredient_list)

    return ingredient_list


def get_deduced_ingredients(ingredient_list):
    # ingredients = []
    # for elem in ingredient_list:
    #     elem2 = word_tokenize(elem.lower())
    #     for part in elem2:
    #         ingredients.append(part)
    #
    # with open("assets/ml_model/model", 'rb') as file:
    #     model = pickle.load(file)
    #
    # results = model.most_similar(positive=ingredients)
    # ingredients.append(results[0])
    # ingredients.append(results[1])
    #
    # data_file1 = pd.read_csv("assets/ml_model/list.csv")
    # counting_efects = np.zeros(len(data_file1.index))
    #
    # for index, row in data_file1.iterrows():
    #     for item in row:
    #         if item in ingredients:
    #             counting_efects[index] += 1
    # max_elem = np.amax(counting_efects)
    #
    # indexes = []
    # for i, elem in enumerate(counting_efects):
    #     if elem == max_elem:
    #         indexes.append(i)
    #
    # data_file2 = pd.read_csv('assets/ml_model/all_drinks.csv')
    # data_file3 = pd.read_csv('assets/ml_model/csv_file.csv')
    # ser2 = pd.Series(data_file2['strDrink'])
    # ser3 = pd.Series(data_file3['list of ingedients'])
    #
    # if len(indexes) == 1:
    #     output = dict(ingredient1=results[0], ingredient2=results[1], drink1_name=ser2[indexes[0]],
    #                   drink1=ser3[indexes[0] + 1], drink2_name='NaN', drink2='NaN')
    # else:
    #     found_indx = random.sample(indexes, 2)
    #     output = dict(ingredient1=results[0], ingredient2=results[1], drink1_name=ser2[indexes[0]],
    #                   drink1=ser3[indexes[0] + 1], drink2_name=ser2[indexes[1]], drink2=ser3[indexes[1] + 1])
    #
    # return output
    pass

