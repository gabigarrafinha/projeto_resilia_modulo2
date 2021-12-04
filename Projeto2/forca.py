import random
from palavras import palavras



def peg_palavra():
    palavra = random.choice(palavras)
    return palavra


def jogar(palavra):
    comp_palavra = " _ " * len(palavra)
    adv = False
    print(palavra)
    letras_adv = []
    palavras_adv = []
    tentativas = 6
    print("Vamos jogar o jogo da Forca!")
    print(enforcado(tentativas))
    print(comp_palavra)
    print("\n")
    while not adv and tentativas > 0:
        adv2 = input("Por favor, chute uma palavra ou uma letra: ").upper()
        if len(adv2) == 1 and adv2.isalpha():
            if adv2 in letras_adv:
                print("Você já acertou essa letra!", adv2)
            elif adv2 not in palavra:
                print(adv2, "não está na palavra :( ")
                tentativas -= 1
                palavras_adv.append(adv2)
            else:
                print("Certa resposta,", adv2, "está na palavra!")
                letras_adv.append(adv2)
                lista_palavras = list(comp_palavra)
                indices = [i for i, letra in enumerate(palavra) if letra == adv2]
                for index in indices:
                    lista_palavras[index] = adv2
                comp_palavra = "".join(lista_palavras)
                if "_" not in comp_palavra:
                    adivinhou = True
        elif len(adv2) == len(palavra) and adv2.isalpha():
            if adv2 in palavras_adv:
                print("Você já acertou a palavra ", adv2)
            elif adv2 != palavra:
                print(adv2, "não é a palavra.")
                tentativas -= 1
                palavras_adv.append(adv2)
            else:
                adivinhou = True
                comp_palavra = palavra
        else:
            print("Não é uma escolha válida, tente novamente.")
        print(enforcado(tentativas))
        print(comp_palavra)
        print("\n")
    if adivinhou:
        print("Parabéns, você acertou a palavra !!")
    else:
        print("Sinto muito, suas tentativas acabaram, a palavra era " + palavra + ". Quem sabe na próxima!")

def enforcado(tentativas):
    fases = [  # cabeça corpo braço2 perna2
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # cabeça corpo braço2 perna
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # cabeça corpo braço2
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # cabeça corpo braço
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # cabeça e corpo
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # cabeça
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # início - vazio
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return fases[tentativas]

def main():
    palavra = peg_palavra()
    jogar(palavra)
    while input("Deseja jogar denovo? (Y/N) ").upper() == "Y":
        palavra = peg_palavra()
        jogar(palavra)


if __name__ == "__main__":
    main()


main()