import random
from funcoes import *

print("***** Bem vindo ao jogo da forca! *****")
print("\n*** Tututorial: ***")
print("O Jogo irá gerar uma palavra secreta, você irá digitar as letras para tentar adivinhar a palavra")
print("Cada acerto aparecerá como dica, você pode errar 5 vezes antes de ser enforcado!")
print("*** Boa sorte! ***\n")

jogar_novamente = 1
while (jogar_novamente == 1):
    print("Escolha a dificuldade que deseja")
    print("(1)- Fácil ou (2)- Difícil (palavras mais longas)")
    dificuldade = int(input("Escolha a opção desejada: "))

    enforcado = False
    acertou = False
    numero_tentativas = 0

    if (dificuldade == 1):
        palavra_secreta = gera_palavra_secreta()
    elif(dificuldade == 2):
        palavra_secreta = gera_palavra_secreta_dificil()
    else:
        while (dificuldade < 1 or dificuldade > 2):
            print("Opção inválida, tente novamente!")
            dificuldade = int(input("Escolha a opção desejada: "))
    acertos = ["_" for letra in palavra_secreta]

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
            print("\n {}".format(acertos))
        enforcado = numero_tentativas == 6
        acertou = "_" not in acertos

    if(acertou):
        print("Parabéns, você acertou, a palavra secreta era {}".format(palavra_secreta))
    else:
        print("Você não acertou a palavra secreta!")
        print("A palavra secreta era {]".format(palavra_secreta))

    print("\nDeseja jogar novamente?")
    print("Digite (1)-Sim   (2)-Não ")
    jogar_novamente = int(input("Escolha sua opção: "))

    while (jogar_novamente < 1 or jogar_novamente > 2):
        print("\nopção inválida, digite novamente ")
        jogar_novamente = int(input("Escolha sua opção: "))


