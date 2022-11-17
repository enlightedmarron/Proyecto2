import random

def Dictsustantivos():
    import random
    sustantivos = ("amor","cafe","equipo","explosion","guitarra","plastico","crema","martillo","libros","lapiz","temor","aluminio","embarcacion","letra","miel","archipielago","rueda","discoteca","universidad","libreria","perros","llaves","manada","pelo","papa","sillon","felicidad","cuna","teclado","servilleta","escuela","pantalla","gente","lapicera","tenedor","estadistica","mapa","fauna","mensaje","lima","cohete","rey","edificio","cesped","presidencia","hojas","familia","colegio","granizo","pestana","lampara","mano","salud","flor","musica","hombre","tornillo","habitacion","velero","abuela","guerra","palo","satelite","templo","lentes","boligrafo","plato","nube","gobierno","botella","castillo","pinar","riqueza","verano","persona","planeta","televisor","guantes","metal","poder","elegancia","mono","remera","muela","petroleo","percha","remate","debate","tiempo","cuaderno","ruido","pared","suerte","herramienta","cartas","chocolate","anteojos","impresora","caramelos","living","luces","angustia","zapato","bomba","racimo","ojo","corbata","ceremonia","alma","planta","odio","buzo","oficina","persiana","puerta","tio","silla","ensalada","pradera","zoologico","candidato","deporte","recipiente","diarios","fotografia","ave","hierro","refugio","pantalon","religion","carne","nieve","tecla","humedad","tropa","departamento","celular","tristeza","hipopotamo","vocabulario","cama","gas","coro","campera","discurso","autos","cinturon","entusiasmo","famoso","madera","fideos","piso","maletin","reloj","diputado","cuchillo","oscuridad","candado","luz","computadora","radio","mono","cuadro","calor","partido","teatro","clientela","fiesta","auriculares")
    sust = random.randint(1,len(sustantivos) - 1)
    return (sustantivos[sust])

esp_set = "            /&@)"

def espace(cadena1, cadena2):
    espacios = random.randint(1, 3)
    esp_char = ""
    s = ""

    s = cadena1
    while (espacios):
        esp_char = esp_set[random.randint(0, 15)]
        s = s + esp_char
        espacios = espacios - 1
    s = s +  "".join(cadena2)
    return s

char_set_v = "aeiouy"
char_set_c = "bcdfghijklmnopqrstvwxz"

def generate_conectores():
    gen_str = ""
    size = random.randint(1, 3)
    is_vocal = random.randint(0, 1)

    if (size == 1):
        is_vocal = True
    while (size != 0):
        if (is_vocal):
            gen_str += "".join(char_set_v[random.randint(0, 5)])
        else :
            gen_str = gen_str + "".join(char_set_c[random.randint(0, 21)])
        size = size - 1
        is_vocal = not is_vocal
    return gen_str

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
    return x

def generador_sustantivos():
    x = random.choice(nouns)
    return x

def generador_preposiciones():
    x = random.choice(prepo)
    return x

def generador_lugares():
    x = random.choice(lugares)
    return x

def generador_adverbios():
    x = random.choice(adv)
    return x

def generador_nombrespersonales():
    x = random.choice(nombrespersonales)
    return x

def alterar_palabra(palabra):
    x = ""
    for i in range(len(palabra)):
        if (random.randint(1, 10) % 3 == 0):
            x += palabra[i].upper()
        else:
            x += palabra[i]
    return x

def select_verbo():
    return random.choice(verbos)

def convert_participio(verbo):
    if (verbo[len(verbo) - 2] == 'a' and verbo[len(verbo) - 1] == 'r'):
        return (verbo.replace('ar', 'ado'))
    if (verbo[len(verbo) - 2] == 'e' and verbo[len(verbo) - 1] == 'r'):
        return (verbo.replace('er', 'ido'))
    if (verbo[len(verbo) - 2] == 'i' and verbo[len(verbo) - 1] == 'r'):
        return (verbo.replace('ir', 'ido'))

def generar_verbo():
    n = random.randint(3, 10)
    c='bcdfgjlmnprstvz'
    v='aeiou'
    sufix= ["ar", "er", "ir"]
    palabra=''
    for j in range(n -1):
        palabra+=''.join(random.choice(c))
        palabra+=''.join(random.choice(v))
    palabra+=''.join(random.choice(sufix))
    return palabra

def generador():
    numero_de_palabras = random.randint(25, 200)
    key_de_palabra = random.randint(0, 10)
    s = ""
    temp = ""

    while (numero_de_palabras):
        if (key_de_palabra == 0):
            temp = Dictsustantivos()
        if (key_de_palabra == 1):
            temp = generador_adjetivos()
        if (key_de_palabra == 2):
            temp = generador_adverbios()
        if (key_de_palabra == 3):
            temp = generador_lugares()
        if (key_de_palabra == 4):
            temp = generador_nombrespersonales()
        if (key_de_palabra == 5):
            temp = generador_preposiciones()
        if (key_de_palabra == 6):
            temp = generador_sustantivos()
        if (key_de_palabra == 7):
            temp = generar_verbo()
        if (key_de_palabra == 8):
            temp = generate_conectores()
        if (key_de_palabra == 9):
            temp = convert_participio(generar_verbo())
        if (key_de_palabra == 10):
            temp = select_verbo()
        if (numero_de_palabras != 1):
            s = espace(s, temp)
        numero_de_palabras = numero_de_palabras - 1
    return s

print(generador())