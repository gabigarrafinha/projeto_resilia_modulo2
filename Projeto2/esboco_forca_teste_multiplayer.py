import random


#inicialização de variáveis e estruturas de dados

jogadores = []
enforcou = False
acertou = False
errou = False
erros = 0
palavra_secreta = ""
palavras_secretas = []
letras_acertadas = []
lista_letras_acertadas = []
#jogador_palavra = {}
#palavras_letras = {}


#função que cria a lista de jogadores
def cria_lista_jogadores():
    quantidade_jogadores = int(input("Escolha a quantidade de jogadores. De 2 a 5: "))
    for n in range(0, (quantidade_jogadores)):
        jogadores.append(input("Qual o nome do jogador?"))

#função que atrubui uma palavra a ser acertada para cada jogador, cria uma lista com elas, e um segunda lista com as lacunas a serem preenchidas pelas letras de cada palavra
def define_palavras():
    for jogagor in jogadores: 
        palavra_secreta = carrega_palavra_secreta()
        palavras_secretas.append(palavra_secreta)
        letras_acertadas = ["_" for letra in palavra_secreta]
        lista_letras_acertadas.append(letras_acertadas)

#função que sorteia a plavra a ser acertada, usei uma lista comum, depois podemos importar de um arquivo
def carrega_palavra_secreta():
    palavras = ['abacaxi', 'paralelepípedo', 'donzela', 'itinerante', 'ornitorrinco']
    palavra_secreta = random.choice(palavras)
    return palavra_secreta.upper()

#função que pede que o jogador chute uma letra da palavra
def pede_palpite():
    palpite = input("Qual letra? ")
    palpite = palpite.upper()
    return palpite

#função que marca os acertos do jogdador. Ela tem parâmetros, o palpite, as letras que ele acertou, e a palavra secreta do jogador. 
def marca_acertos(palpite, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (palpite == letra):
            letras_acertadas[index] = letra
        index += 1

#função para saudar o vencedor, acabei tirando nos testes do multiplayer, mas depois podemos usar de novo.
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
  
#função que exibe a mensagem quando a pessoa é enforcada, acabei tirando nos testes do multiplayer, mas depois podemos usar de novo.
def imprime_mensagem_perdedor(palavra_secreta):
    print("Você foi enforcado!")
    

#função que desena a forca
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#função do jogo
def jogar():

    enforcou = False
    acertou = False
    errou = False
    fim_do_jogo = False
    erros = 0
    

    print("Vamos jogar o jogo da Forca!")

    cria_lista_jogadores()

    define_palavras()

    #dicionario que criei para tentar fazer o laço funcionar, mas ainda não testei muito
    #palavras_letras = dict(zip(palavras_secretas, lista_letras_acertadas))
    #jogador_palavra = dict(zip(jogadores, palavras_secretas))
    #print(jogador_palavra)
    #print(palavras_letras)
    

    while not fim_do_jogo:

        #criei uma variável do índice para ser usada no laõ realcionando a posição do jogador na lista com a posição da palavra secreta dele e das letras acertadas dele.
        #a ideia é incrimentar ele durante o for, mas zerar quando o primeiro while começa de novo, para não dar 'out of index'
        indice = 0

        for jogador in jogadores: 

            print(lista_letras_acertadas[indice])

            letras_faltando = len(lista_letras_acertadas[indice])

    
            while (not acertou and not enforcou and not errou):
                
                print(jogador, 'é a sua vez')

                #mandei imprimir o índice para ver se estava certa a numeração
                print('O índice é: ', indice)
                palpite = pede_palpite()

                if (palpite in palavras_secretas[indice]):
                    marca_acertos(palpite, lista_letras_acertadas[indice], palavras_secretas[indice])
                    letras_faltando = str(lista_letras_acertadas[indice].count('_'))
                    if (letras_faltando == "0"):
                        print("PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(palavras_secretas[indice].upper()))
                else:
                    erros += 1
                    print(lista_letras_acertadas[indice])
                    break

                enforcou = erros == 7
                errou = erros > 0
                acertou = "_" not in lista_letras_acertadas[indice]    

                print(lista_letras_acertadas[indice])

            if (acertou):
                fim_do_jogo = True
                    #imprime_mensagem_vencedor()
            elif enforcou:
                print("Você foi enforcado")
                print("A palavra era", palavras_secretas[indice])
                jogadores.pop(indice)
            else:
                print('Você errou')
                print('Ainda faltam acertar', letras_faltando, 'letras')
                desenha_forca(erros)
                
            indice += 1

    print("Fim do jogo")


""" Aqui eu chamo as funções em separado para testar quando preciso

cria_lista_jogadores()

define_palavras()

print(palavras_secretas)
print(lista_letras_acertadas)

letras_faltando = str(lista_letras_acertadas[0].count('_'))

print(letras_faltando) """


jogar()