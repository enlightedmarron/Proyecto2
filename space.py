import random

esp_set = "       /&@)"

def suma(cadena1, cadena2):
    espacios = random.randint(1, 5)
    esp_char = ""
    s = ""

    s = cadena1
    while (espacios):
        esp_char = esp_set[random.randint(0, 10)]
        s = s + esp_char
        espacios = espacios - 1
    s = s +  "".join(cadena2)
    return s

print(suma("cadena1", "cadena2"))