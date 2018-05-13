from slpp import slpp as lua

with open('raw/technology.lua', 'r') as handle:
    technology_list = handle.readlines()

# Strip out unused logic
x = 0
while x < len(technology_list):
    line = technology_list[0]
    if line == 'data:extend(':
        print(line)
    x += 1

technology_string = ''.join(technology_list)
print(technology_string)
technology = lua.decode(technology_string)
print(len(technology))
