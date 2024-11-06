import random;

RU = 98
EN = 1
EU = 0.9
KZ = 490
BR = 3
curse=[
{'name': 'RU', 'zena': 98}, 
{'name': 'EN', 'zena': 1}, 
{'name': 'EU', 'zena': 0.9}, 
{'name': 'KZ', 'zena': 490}, 
{'name': 'BR', 'zena': 3}
]
SCHET = 0
while (curse[4]['zena'] <= curse[0]['zena']):
    curse[4]['zena'] +=  random.randint(-5,10)
    for i in range(len(curse)):
        print(curse[i]['name'], curse[i]['zena'])