from random import choice

lista_palavras = ["sol", "montanha", "programacao", "livro", "oceano", "nuvem", "teclado",
                  "tela", "cidade", "arvore", "codigo", "musica", "janela", "porta", "luz",
                  "sombras", "caminho", "viagem", "tempo", "historia"]

palavra_escolhida = choice(lista_palavras)
palavra_oculta = ["-"] * len(palavra_escolhida)


def escolher_letra():
    letra = input("Digite uma letra que você acha que está na palavra: ")

    while len(letra) != 1 or not letra.isalpha():
        letra = input("Por favor, digite apenas UMA letra válida: ")

    return letra.lower()


def validar_letra(letra, palavra):
    indices = []

    for i, letra_atual in enumerate(palavra):
        if letra_atual == letra:
            indices.append(i)

    return indices


def atualizar_palavra(indices, letra, estado):
    for i in indices:
        estado[i] = letra


def jogo_principal(estado, palavra):

    tentativas = 6
    letras_usadas = []

    print(" ".join(estado))

    while tentativas > 0:

        letra = escolher_letra()

        if letra in letras_usadas:
            print("Essa letra já foi usada, tente outra.")
            continue

        letras_usadas.append(letra)

        indices = validar_letra(letra, palavra)

        if not indices:
            tentativas -= 1
            print(f"A letra não está na palavra. Restam {tentativas} tentativas | letras usadas [{', '.join(letras_usadas)}]")

        atualizar_palavra(indices, letra, estado)

        print(" ".join(estado))

        if "-" not in estado:
            print("Parabéns, você venceu!")
            break

    if tentativas == 0:
        print(f"Você perdeu! A palavra era: {palavra}")


jogo_principal(palavra_oculta, palavra_escolhida)