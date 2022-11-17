import random
from sys import exit
with open("diccionario/verbos.txt", 'r') as f:
    verb = f.read().splitlines()

def select_verbo():
    return random.choice(verb)

def convert_participio(verbo):
    if (verbo[len(verbo) - 2] == 'a' and verbo[len(verbo) - 1] == 'r'):
        return (verbo.replace('ar', 'ado'))
    if (verbo[len(verbo) - 2] == 'e' and verbo[len(verbo) - 1] == 'r'):
        return (verbo.replace('er', 'ido'))
    if (verbo[len(verbo) - 2] == 'i' and verbo[len(verbo) - 1] == 'r'):
        return (verbo.replace('ir', 'ido'))

def generar_verbo(n):
    c='bcdfgjlmnprstvz'
    v='aeiou'
    sufix= ["ar", "er", "ir"]
    palabra=''
    for j in range(n -1):
        palabra+=''.join(random.choice(c))
        palabra+=''.join(random.choice(v))
    palabra+=''.join(random.choice(sufix))
    return palabra