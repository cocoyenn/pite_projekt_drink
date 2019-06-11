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
    from gensim.models import Word2Vec
    
    
    with open('ml_model/model', 'rb') as file:
        model = pickle.load(file)
    
    
    results = model.wv.most_similar(positive = ingredients.lower)
    
    output  = dict(drink1:results[0], drink2:results[1])
    
    return output
