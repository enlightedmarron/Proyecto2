import ramdom
from Dicsustantivos.py import Dictsustantivos
from conectores.py import generate_conectores
from space.py import space
from verbos.py import verbos

def genrator():
    al = random.randint(1,2)
    final = "";
    final = final.join(Dicsustantivos())
    final = final.join(space())
    if al == 1)
        final = final.join(verbos())
    else:
        final = final.join(adjetivo())
    al = random.randint(1,2);
    final = final.join(adjetivo())
    final = final.join(espacio)
    final = final.join(conecto())
    final = final.join(espacio)
    if al == 1:
        final = final.join(adjetivo())
    else
        final = final.join(sustantivo());
    return (final)

number = random.randint(5,20)
for range(1,number):
    print(generator())
