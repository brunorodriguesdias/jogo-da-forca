import random

enforcado = False
acertou = False
numero_tentativas = 0



with open("palavras.txt", "r") as arquivo:
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero].upper()

acertos = ["_" for letra in palavra_secreta]

print("***** Bem vindo ao jogo da forca! *****")
print("\n*** Tututorial: ***")
print("O Jogo irá gerar uma palavra secreta, você irá digitar as letras para tentar adivinhar a palavra")
print("Cada acerto, aparecerá como dica, você pode errar 5 vezes antes de ser enforcado!")
print("*** Boa sorte! ***\n")

print(acertos)
