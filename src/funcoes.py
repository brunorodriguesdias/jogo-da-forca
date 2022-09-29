import random

def gera_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
def gera_palavra_secreta_dificil():
    with open("palavras_dificeis.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
def consulta_acerto(palavra_secreta, tentativa, acertos):
    i = 0
    for letra in palavra_secreta:
        if (tentativa.upper() == letra.upper()):
            acertos[i] = letra
        i += 1
    print(acertos)


def impressao_forca(numero_tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(numero_tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(numero_tentativas == 2):
        print(" |      (_)   ")
        print(" |      /     ")
        print(" |            ")
        print(" |            ")

    if(numero_tentativas == 3):
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")

    if(numero_tentativas == 4):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |            ")
        print(" |            ")

    if(numero_tentativas == 5):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      /     ")

    if(numero_tentativas == 6):
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      / \    ")

    print(" |            ")
    print("_|___         ")
    print()
    print("***       DICA       ***")
    print("A palavra está em uma dessas categorias: animais, frutas ou legumes, países\n")