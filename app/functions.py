import csv


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


def generate_drinks(ingredient_list):

    return ingredient_list
