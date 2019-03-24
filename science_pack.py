"""
Generate a list of all materials needed to produce science packs
"""

import copy
import csv
import pprint


def read_recipes():
    recipes = {}
    with open('data/recipes.csv') as handle:
        reader = csv.reader(handle)
        for row in reader:
            recipes[row[0]] = row[1:]
    return recipes


def get_science_packs(recipes):
    science_packs = [r for r in recipes.keys() if 'science-pack' in r]
    science_packs += ['satellite', 'rocket-part']
    recipes['science-packs'] = science_packs


def get_dependencies(recipe, recipes):
    if recipe == 'solid-fuel':
        return ['heavy-oil', 'light-oil', 'petroleum-gas']
    return recipes.get(recipe, [])


def traverse_list(dependency, recipes):
    dependencies = [dependency]
    i = 0
    while i < len(dependencies):
        dependencies += [r for r in get_dependencies(dependencies[i], recipes) if r not in dependencies]
        i += 1
    return dependencies

def traverse_tree(dependency):
    children = get_dependencies(dependency)
    children = [traverse_tree(d) for d in children]
    return {dependency: children}

recipes = read_recipes()
get_science_packs(recipes)
dependencies = traverse_list('science-packs', recipes)
[print(d) for d in dependencies]
