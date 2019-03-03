import csv
import os
import pprint

from slpp import slpp as lua


files = os.listdir('raw/recipe')
recipes_string = ''
for filename in files:
    with open('raw/recipe/%s' % filename, 'r') as handle:
        recipes_string += handle.read() + ','

recipes_string = '{' + recipes_string[:-1] + '}'
recipes = lua.decode(recipes_string)
recipes = [r for d in recipes for r in d]
recipes = [r for r in recipes if r != ')']


def return_recipe_dependency_tree(recipes):
    tree = {}
    for x in range(len(recipes)):
        recipe = recipes[x]
        if type(recipe) == str:
            continue
        name = recipe['name']
        if 'ingredients' in recipe:
            ingredients = recipe['ingredients']
        if 'normal' in recipe:
            ingredients = recipe['normal'].get('ingredients', [])
        dependencies = []
        for x in ingredients:
            if 'name' in x:
                dependencies.append(x['name'])
            else:
                dependencies.append(x[0])
        tree[name] = dependencies
    return tree


def save_recipe_dependency_tree(tree):
    matrix = []
    for key, value in tree.items():
        row = [key] + value
        matrix.append(row)
    matrix = sorted(matrix, key=lambda x: x[0])
    matrix = sorted(matrix, key=lambda x: len(x))
    with open('data/recipes.csv', 'w') as handle:
        writer = csv.writer(handle)
        for row in matrix:
            writer.writerow(row)


tree = return_recipe_dependency_tree(recipes)
save_recipe_dependency_tree(tree)
print('Wrote %s items' % len(tree))
