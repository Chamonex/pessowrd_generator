import string
import random

senha =""

caracteres = {
    0: [string.ascii_letters, len(string.ascii_letters)],
    1: [string.digits, len(string.digits)],
    2: [string.punctuation, len(string.punctuation)]
}

def generate_password(senha):

    for i in range(10):

        x = random.randint(0, 2)
        y = random.randint(0, caracteres[x][1])
        novo = caracteres[x][0][random.randint(0, y)]
        senha += novo

print(senha)

