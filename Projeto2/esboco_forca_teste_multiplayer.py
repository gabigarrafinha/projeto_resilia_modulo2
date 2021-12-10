import random
from string import ascii_letters
from palavras import palavras
from boneco_forca import desenha_forca


#inicialização de variáveis e estruturas de dados

jogadores = []
enforcou = False
ganhou = False
errou = False
erros = []
palavra_secreta = ""
palavras_secretas = []
letras_acertadas = []
lista_letras_acertadas = []
#jogador_palavra = {}
#palavras_letras = {}

#função que criei para pausar o código nas partes que estavam dando erro para poder analisar o corportamento dos laços
def pause():
    input("Pressione <enter> para continuar" )

#função que cria a lista de jogadores
def cria_lista_jogadores():
    quantidade_jogadores = input("Escolha a quantidade de jogadores. De 2 a 5: ")
    if not quantidade_jogadores.isdigit():
        print("Por favor, digite uma opção válida!\n")
        quantidade_jogadores = 0
        cria_lista_jogadores()
    elif int(quantidade_jogadores) < 2 or int(quantidade_jogadores) > 5:
        print("Por favor, digite uma opção válida!\n")
        quantidade_jogadores = 0
        cria_lista_jogadores()
    for n in range(0, (int(quantidade_jogadores))):
        jogadores.append(input("Qual o nome do jogador?\n "))

#função que atrubui uma palavra a ser acertada para cada jogador, cria uma lista com elas, e um segunda lista com as lacunas a serem preenchidas pelas letras de cada palavra
def define_palavras():
    for jogador in jogadores: 
        palavra_secreta = carrega_palavra_secreta()
        palavras_secretas.append(palavra_secreta)
        letras_acertadas = ["_" for letra in palavra_secreta]
        lista_letras_acertadas.append(letras_acertadas)
        erros.append(0)

#função que sorteia a plavra a ser acertada, usei uma lista comum, depois podemos importar de um arquivo
def carrega_palavra_secreta():
    palavra_secreta = random.choice(palavras)
    return palavra_secreta.upper()

#função que pede que o jogador chute uma letra da palavra
def pede_palpite():
    palpite = input("Qual letra?\n ")
    if palpite not in ascii_letters:
        print("Por favor, digite uma letra alfabeto")
        pede_palpite()
    else:
        palpite = palpite.upper()
    return palpite

#função que marca os acertos do jogdador. Ela tem parâmetros, o palpite, as letras que ele ganhou, e a palavra secreta do jogador. 
def marca_acertos(palpite, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (palpite == letra):
            letras_acertadas[index] = letra
        index += 1

#função para saudar o vencedor, acabei tirando nos testes do multiplayer, mas depois podemos usar de novo.
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!\n")
  
#função que exibe a mensagem quando a pessoa é enforcada, acabei tirando nos testes do multiplayer, mas depois podemos usar de novo.
def imprime_mensagem_perdedor(palavra_secreta):
    print("Você foi enforcado!\n")
    

#função do jogo
def jogar():

    enforcou = False
    ganhou = False
    errou = False
    fim_do_jogo = False
    

    print("Vamos jogar o jogo da Forca!")

    cria_lista_jogadores()

    define_palavras()
    
    while not fim_do_jogo:

        #criei uma variável do índice para ser usada no laço realcionando a posição do jogador na lista com a posição da palavra secreta dele e das letras acertadas dele.
        #a ideia é incrimentar ele durante o for, mas zerar quando o primeiro while começa de novo, para não dar 'out of index'
        indice = 0

        print(jogadores)

        if jogadores == []:
           fim_do_jogo = True
        else:


            for jogador in jogadores: 

                print(lista_letras_acertadas[indice])

                letras_faltando = len(lista_letras_acertadas[indice])

                desenha_forca(erros[indice])


                #reset da variável boleana que diz se a pessoa errou a rodada, porque se não for zerada o laço não termina
                errou_palpite = False
                
                #reset da variável boleana que diz se a pessoa foi enforcada, porque se não for zerada quando o primeiro é enforcado o jogo termina para todos
                enforcou = False

            
                while (not ganhou and not enforcou and not errou_palpite):
                        
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
                        erros[indice] += 1
                        print(lista_letras_acertadas[indice])
                        errou_palpite = True
                            
                    
                            
                    #print(erros[indice])
                    enforcou = erros[indice] == 7
                    #print(enforcou)
                    #errou = erros[indice] > 0 and erros[indice] < 7
                    ganhou = "_" not in lista_letras_acertadas[indice]    

                    print(lista_letras_acertadas[indice])


                if (ganhou):
                    fim_do_jogo = True
                                
                elif (enforcou):
                    #print(erros[indice])
                    desenha_forca(erros[indice])
                    print("Você foi enforcado")
                    print("A palavra era", palavras_secretas[indice])
                    jogadores.remove(jogador)
                    erros.pop(indice)
                    palavras_secretas.pop(indice)
                elif (errou_palpite):
                    print('Você errou')
                    print('Ainda faltam acertar', letras_faltando, 'letras')
                    desenha_forca(erros[indice])
                        
                indice += 1

    print("Fim do jogo")




jogar()