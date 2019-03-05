"""
Generate a list of all materials needed to produce science packs
"""

import csv

recipes = {}
with open('data/recipes.csv') as handle:
    reader = csv.reader(handle)
    for row in reader:
        recipes[row[0]] = row[1:]

science_packs = [r for r in recipes.keys() if 'science-pack' in r]
print(science_packs)


def get_dependencies(recipe):
    if recipe == 'solid-fuel':
        return ['heavy-oil', 'light-oil', 'petroleum-gas']
    return recipes.get(recipe, [])


dependencies = science_packs
i = 0
while i < len(dependencies):
    dependencies += [r for r in get_dependencies(dependencies[i]) if r not in dependencies]
    i += 1

print(dependencies)
