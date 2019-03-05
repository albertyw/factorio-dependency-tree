"""
Generate a list of all materials needed to produce science packs
"""

import copy
import csv
import pprint

recipes = {}
with open('data/recipes.csv') as handle:
    reader = csv.reader(handle)
    for row in reader:
        recipes[row[0]] = row[1:]

science_packs = [r for r in recipes.keys() if 'science-pack' in r]
print(science_packs)
recipes['science-packs'] = science_packs


def get_dependencies(recipe):
    if recipe == 'solid-fuel':
        return ['heavy-oil', 'light-oil', 'petroleum-gas']
    return recipes.get(recipe, [])


def traverse_list(dependency):
    dependencies = [dependency]
    i = 0
    while i < len(dependencies):
        dependencies += [r for r in get_dependencies(dependencies[i]) if r not in dependencies]
        i += 1
    return dependencies

def traverse_tree(dependency):
    children = get_dependencies(dependency)
    children = [traverse_tree(d) for d in children]
    return {dependency: children}


dependencies = traverse_list('science-packs')
[print(d) for d in dependencies]
