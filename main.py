import string
import random

caracteres = {
    0: [string.digits, len(string.digits)],
    1: [string.ascii_letters, len(string.ascii_letters)],
    2: [string.punctuation, len(string.punctuation)]
}

def generate_password(option):

    password =""

    if option == 1:                     #somente numeros
        for i in range(10):
            m = caracteres[0][1]
            new = caracteres[0][0][random.randint(0, m)]
            password += new

        return password

    elif option == 2:                   #numeros e letras
        for i in range(10):
            x = random.randint(0, 1)
            m = caracteres[x][1]
            new = caracteres[x][0][random.randint(0, m)]
            password += new

        return password

    else:
        for i in range(10):             #nueros, letras e pontuação

            x = random.randint(0, 2)
            m = caracteres[x][1]
            new = caracteres[x][0][random.randint(0, m)]
            password += new

        return password


print("1 -> somente numeros\n2 -> numeros e letras\n3 -> nomeros letras e pontuacao\n")


option = input()

print(generate_password(option))

