import random
import string
5
def key_generator():
    """ generador serial de claves """
    cant_key = int(input('Ingrese la cantidad de Seriales que necesita: '))
    choices = string.ascii_uppercase + string.digits
    for i in range(cant_key):
        key_chars = []
        for j in range(5):
            key_chars.append(''.join(random.choice(choices) for i in range(5)))
        key = '-'.join(key_chars)
        print(key)

key_generator()
