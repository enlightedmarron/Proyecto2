import random

def Dictsustantivos():
    sustantivos = ("amor","cafe","equipo","explosion","guitarra","plastico","crema","martillo","libros","lapiz","temor","aluminio","embarcacion","letra","miel","archipielago","rueda","discoteca","universidad","libreria","perros","llaves","manada","pelo","papa","sillon","felicidad","cuna","teclado","servilleta","escuela","pantalla","gente","lapicera","tenedor","estadistica","mapa","fauna","mensaje","lima","cohete","rey","edificio","cesped","presidencia","hojas","familia","colegio","granizo","pestana","lampara","mano","salud","flor","musica","hombre","tornillo","habitacion","velero","abuela","guerra","palo","satelite","templo","lentes","boligrafo","plato","nube","gobierno","botella","castillo","pinar","riqueza","verano","persona","planeta","televisor","guantes","metal","poder","elegancia","mono","remera","muela","petroleo","percha","remate","debate","tiempo","cuaderno","ruido","pared","suerte","herramienta","cartas","chocolate","anteojos","impresora","caramelos","living","luces","angustia","zapato","bomba","racimo","ojo","corbata","ceremonia","alma","planta","odio","buzo","oficina","persiana","puerta","tio","silla","ensalada","pradera","zoologico","candidato","deporte","recipiente","diarios","fotografia","ave","hierro","refugio","pantalon","religion","carne","nieve","tecla","humedad","tropa","departamento","celular","tristeza","hipopotamo","vocabulario","cama","gas","coro","campera","discurso","autos","cinturon","entusiasmo","famoso","madera","fideos","piso","maletin","reloj","diputado","cuchillo","oscuridad","candado","luz","computadora","radio","mono","cuadro","calor","partido","teatro","clientela","fiesta","auriculares")
    sust = random.randint(1,len(sustantivos) - 1)
    return (sustantivos[sust])