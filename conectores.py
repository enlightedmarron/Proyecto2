from numpy import random as rd

char_set_v = "aeiouy"
char_set_c = "bcdfghijklmnopqrstvwxz"

def generate_conectores():
    gen_str = ""
    size = rd.randint(1, 3)
    is_vocal = rd.randint(0, 1)

    if (size == 1):
        is_vocal = True
    while (size != 0):
        if (is_vocal):
            gen_str = gen_str + "".join(char_set_v[rd.randint(5)])
        else :
            gen_str = gen_str + "".join(char_set_c[rd.randint(22)])
        size = size - 1
        is_vocal = not is_vocal
    return gen_str

print(generate_conectores()) 