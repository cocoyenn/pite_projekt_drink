import csv


def get_ingredients_list():

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

    return ingredients


def prepare_ingredients_list(request):
    ingredient_list = []

    for elementId, ingredient in request.POST.items():
        ingredient_list.append(str(ingredient))

    ingredient_list.pop(0)

    return ingredient_list


def generate_drinks(ingredient_list):
    import pickle
    import nltk
    import csv
    import random
    import numpy as np
    from gensim.models import Word2Vec
    
    ingredients = nltk.word_tokenize(ingredients[:].lower)
    
    
    with open('ml_model/model', 'rb') as file:
        model = pickle.load(file)
    
    results = model.wv.most_similar(positive = ingredients)
    ingredients.append(results[0])
    ingredients.append(results[1])
    
    counting_efects = np.zeros(546)
    data_file1      = pd.read_csv('ml_model/list.csv')
    
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
    
    if len(indexes) > 1:
        output = dict(ingredient1:results[0], ingredient2:results[1], drink1_name:ser2[indexes[0]],
                        drink1:ser3[indexes[0]+1], drink2_name:nan, drink2:nan)
    else:
        found_indx = random.sample(indexes, 2)
        output = dict(ingredient1:results[0], ingredient2:results[1], drink1_name:ser2[indexes[0]],
                    drink1:ser3[indexes[0]+1], drink2_name:ser2[indexes[1]], drink2:ser3[indexes[1]+1])
    
    return output
