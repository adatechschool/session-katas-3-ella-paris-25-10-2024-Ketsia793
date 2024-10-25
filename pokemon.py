import json

with open('pokemonGO.json','r') as file:
    data = json.load(file)
    print(data)

# Print the type of data variable
    """print("Type: ", type(data))"""

# Print the data of dictionary
    """print("\npokemon:"),"""
"""data['pokemon']"""



#print(data['pokemon'][0])
def poke_weight():
    print("\nPrinting nested dictionary as a key-value pair\n")
for i in data ['pokemon']:
        print("id", i['id'])
        print("name:", 
i ['name'])
        print("type:", 
i ['type'])
        print("weight:", 
i ['weight'])
        
        ['weight'] = map((float, ('weight')))
        if i ['weight'] > 10:
             print("Voici les pokemon dont le poids est supérieur à 10kg")
poke_weight()
        
