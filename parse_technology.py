import csv
import os

from slpp import slpp as lua


"""
files = os.listdir('raw/technology')
technology_string = ''
for filename in files:
    if filename[:5] == 'demo-':
        continue
    with open('raw/technology/%s' % filename, 'r') as handle:
        technology_string += handle.read() + ','

technology_string = '{' + technology_string[:-1] + '}'
technology = lua.decode(technology_string)
technology = [t for d in technology for t in d]
"""


with open('raw/technology/technology.lua', 'r') as handle:
    technology_string = handle.read()
technology_string = '{' + technology_string[:-1] + '}'
technology = lua.decode(technology_string)
technology = [t.values() for t in technology if type(t) == dict]
technology = [t for d in technology for t in d]


def return_tech_dependency_tree(techs):
    tree = {}
    for x in range(len(techs)):
        tech = techs[x]
        if type(tech) == str:
            continue
        name = tech['name']
        dependencies = tech.get('prerequisites', [])
        tree[name] = dependencies
    return tree


def save_tech_dependency_tree(tree):
    matrix = []
    for key, value in tree.items():
        row = [key] + value
        matrix.append(row)
    matrix = sorted(matrix, key=lambda x: x[0])
    matrix = sorted(matrix, key=lambda x: len(x))
    with open('data/technology.csv', 'w') as handle:
        writer = csv.writer(handle)
        for row in matrix:
            writer.writerow(row)


tree = return_tech_dependency_tree(technology)
save_tech_dependency_tree(tree)
print('Wrote %s items' % len(tree))
