import csv
from slpp import slpp as lua


with open('raw/technology2.lua', 'r') as handle:
    technology_string = handle.read()

technology = lua.decode(technology_string)


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
