import random
from string import ascii_letters
from palavras import palavras
from boneco_forca import desenha_forca


#inicialização de variáveis e estruturas de dados

jogadores = []
dicionario_jogadres = {}
enforcou = False
ganhou = False
errou = False
erros = []
palavra_secreta = ""
palavras_secretas = []
letras_acertadas = []
lista_letras_acertadas = []
pontuacao = {}

#função que criei para pausar o código nas partes que estavam dando erro para poder analisar o corportamento dos laços
def pause():
    input("Pressione <enter> para continuar" )


# função que cria um dicionário de jogadores com um id numérico para cada um deles. O dicionário será usada como origem da lista de jogadores da partida 
def cria_dicionario_jogadores():
    quantidade_jogadores = input("Escolha a quantidade de jogadores. De 2 a 5: ")
    if not quantidade_jogadores.isdigit():
        print("Por favor, digite uma opção válida!\n")
        quantidade_jogadores = 0
        cria_dicionario_jogadores()
    elif int(quantidade_jogadores) < 2 or int(quantidade_jogadores) > 5:
        print("Por favor, digite uma opção válida!\n")
        quantidade_jogadores = 0
        cria_dicionario_jogadores()
    id = 1
    for n in range(0, (int(quantidade_jogadores))):
        dicionario_jogadres.update({id : (input("Qual o nome do jogador?\n "))})
        id += 1

#função que cria a lista de jogadores a cada partida
def cria_lista_jogadores():
    for id in dicionario_jogadres.keys():
        jogadores.append(id)


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
    while palavra_secreta in palavras_secretas:
        palavra_secreta = random.choice(palavras)
    return palavra_secreta.upper()

#função que cria a tabela de pontuação
def cria_tabela_pontos():
    for jogador in jogadores:
        pontuacao [jogador] = 0
    return pontuacao

#função que marca pontos do vencedor
def marca_ponto(vencedor):
    pontuacao [vencedor] += 1
    return pontuacao

#função que imprime a pontuação
def imprime_placar():
    for chave, valor in pontuacao.items():
     print(f"O jogador {chave}, {dicionario_jogadres[chave]},  está com {valor} pontos")

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
    
#função que cria método para jogar de novo no fim de jogo
def play_again():
    pergunta = input("Deseja jogar de novo? (Y/N) ")
    while pergunta not in {'Y','N','y','n','1','2'}:
        pergunta = input("Deseja jogar de novo? (Y/N) ")
    if pergunta in {'Y','y','1'}:
        jogadores.clear()
        erros.clear()
        palavras_secretas.clear()
        letras_acertadas.clear()
        lista_letras_acertadas.clear()
        imprime_placar()
        cria_lista_jogadores()
        jogar()
    elif  pergunta in {'N','n','2'}:
        quit()

#função do jogo
def jogar():

    enforcou = False
    ganhou = False
    errou = False
    fim_do_jogo = False
    

    print("Vamos jogar o jogo da Forca!")

    define_palavras()
    
    while not fim_do_jogo:

        #criei uma variável do índice para ser usada no laço realcionando a posição do jogador na lista com a posição da palavra secreta dele e das letras acertadas dele.
        #a ideia é incrimentar ele durante o for, mas zerar quando o primeiro while começa de novo, para não dar 'out of index'
        indice = 0
        

        if jogadores == []:
           fim_do_jogo = True
        else:


            for jogador in jogadores: 

                print(lista_letras_acertadas[indice])

                letras_faltando = len(lista_letras_acertadas[indice])


                #reset da variável boleana que diz se a pessoa errou a rodada, porque se não for zerada o laço não termina
                errou_palpite = False
                
                #reset da variável boleana que diz se a pessoa foi enforcada, porque se não for zerada quando o primeiro é enforcado o jogo termina para todos
                enforcou = False

            
                while (not ganhou and not enforcou and not errou_palpite):
                        
                    print(dicionario_jogadres[jogador], 'é a sua vez')

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
                            
                    enforcou = erros[indice] == 7
                    ganhou = "_" not in lista_letras_acertadas[indice]    

                    print(lista_letras_acertadas[indice])

                if (ganhou):
                    fim_do_jogo = True
                    marca_ponto(jogador)
                    print(pontuacao)
                    break
                                
                elif (enforcou):
                    desenha_forca(erros[indice])
                    print("Você foi enforcado")
                    print("A palavra era", palavras_secretas[indice])
                    jogadores.remove(jogador)
                    erros.pop(indice)
                    palavras_secretas.pop(indice)
                    lista_letras_acertadas.pop(indice)

                elif (errou_palpite):
                    print('Você errou')
                    print('Ainda faltam acertar', letras_faltando, 'letras')
                    desenha_forca(erros[indice])
                        
                indice += 1

    print("Fim do jogo\n")
    play_again()


cria_dicionario_jogadores()

cria_lista_jogadores()

cria_tabela_pontos()

jogar()