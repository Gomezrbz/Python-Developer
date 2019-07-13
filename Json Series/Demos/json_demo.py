import json

# Open the json file in the same directory as the python script and save it on a python object.
with open('states.json')as f:
    data = json.load(f)

# Print the information
for state in data['states']:
    print(state['name'], state['abbreviation'])

# Checking the area codes list of every state
for item in data['states']:
    name = item['name']
    abbreviation = item['abbreviation']
    print(name,abbreviation,':')
    for area in item['area_codes']:
        print(area)

# Delete information from the state object.
for state in data['states']:
    del state['area_codes']

# Open the file and then doing a dump with the data and the file name in which you want to write the data. In this case, the file name is new states.
with open('new_states.json','w') as f:
    json.dump(data,f, indent=2)