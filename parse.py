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
    with open('data/technology.csv', 'w') as handle:
        writer = csv.writer(handle)
        for key, value in tree.items():
            row = [key] + value
            writer.writerow(row)


tree = return_tech_dependency_tree(technology)
save_tech_dependency_tree(tree)
print(len(tree))
