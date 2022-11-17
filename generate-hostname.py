#!/usr/bin/env python

import random
from sys import exit

with open("diccionario/adjetivos.txt", 'r') as f:
    adj = f.read().splitlines()

with open("diccionario/sustantivos.txt", 'r') as f:
    nouns = f.read().splitlines()

with open("diccionario/preposiciones.txt", 'r') as f:
    prepo = f.read().splitlines()

with open("diccionario/lugares.txt", 'r') as f:
    lugares = f.read().splitlines()

with open("diccionario/adverbios.txt", 'r') as f:
    adv = f.read().splitlines()

with open("diccionario/nombres_personales.txt", 'r') as f:
    nombrespersonales = f.read().splitlines()

with open("diccionario/verbos.txt", 'r') as f:
    verbos = f.read().splitlines()

def generador_adjetivos():
    x = random.choice(adj)
    return a

def generador_sustantivos():
    x = random.choice(nouns)
    return a

def generador_preposiciones():
    x = random.choice(prepo)
    return a

def generador_lugares():
    x = random.choice(lugares)
    return a

def generador_adverbios():
    x = random.choice(adv)
    return a

def generador_nombrespersonales():
    x = random.choice(nombrespersonales)
    return a

def generador_verbos():
    x = random.choice(verbos)
    return a

def alterar_palabra(palabra):
    x = ""
    for i in range(len(palabra)):
        if (random.randint(1, 10) % 3 == 0):
            x += palabra[i].upper()
        else:
            x += palabra[i]
    return x

x = generador_sustantivos() + " " + generador_adjetivos() + " " + generador_preposiciones() + " " + generador_lugares()
print(x)

