import random
from funcoes import *

enforcado = False
acertou = False
numero_tentativas = 0

palavra_secreta = gera_palavra_secreta()

acertos = ["_" for letra in palavra_secreta]

print("***** Bem vindo ao jogo da forca! *****")
print("\n*** Tututorial: ***")
print("O Jogo irá gerar uma palavra secreta, você irá digitar as letras para tentar adivinhar a palavra")
print("Cada acerto, aparecerá como dica, você pode errar 5 vezes antes de ser enforcado!")
print("*** Boa sorte! ***\n")

print(acertos)

while(not enforcado and not acertou):
    tentativa = input("Digite uma letra: ")
    tentativa = tentativa.strip().upper()

    if (tentativa in palavra_secreta):
        consulta_acerto(palavra_secreta, tentativa, acertos)
    else:
        numero_tentativas += 1
        print("Você errou, ainda restam {} tentativas".format(6 - numero_tentativas))
        impressao_forca(numero_tentativas)
    enforcado = numero_tentativas == 6
    acertou = "_" not in acertos

if(acertou):
    print("Parabéns, você acertou, a palavra secreta era {}".format(palavra_secreta))
else:
    print("Você não acertou a palavra secreta!")


