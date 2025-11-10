from random import randint

def solicita_palavra():
    '''
    Função que solicita uma entrada do usuário, solicitando uma palavra palavra válida..
        - Retorna:
            palavra (str) - retorna uma palavra validada como alfabética..
    '''
    palavra = input('Insira uma palavra para inclusão na lista de sorteio: ').strip().upper()
    if palavra.isalpha() and palavra != '':
        print('Inserido com sucesso!\n')
    else:
        print(f'Infelizmente [{palavra}] não é válido pra inserir na lista de palavras, tente novamente...\n')
        palavra = ''
    return palavra

def preencher_lista(tamanho):
    '''
    Função que inicia um loop para obter palavras a partir de entradas do usuário, inserindo numa lista, e retornando a lista quando tiver tamanho de acordo com o parâmetro definido.
        - Argumentos:
            tamanho (int) - define o tamanho que a lista terá.
        - Retorna:
            lista (list) - retorna uma lista preenchida com palavras obtidas por 'entrada do usuário'
    '''
    lista = []
    while len(lista) < tamanho:
        palavra = solicita_palavra()
        if palavra != '': 
            lista.append(palavra)
    return lista

def sortear_posicao(lista):
    '''
    Função que recebe uma lista e sorteia uma posicao na lista retornando seu índice.
        - Argumentos:
            lista (list) - recebe uma lista de elementos.
        - Retorna:
            posicao_sorteada (int) - retorna um número de indice sorteado de uma lista.
    '''
    posicao_sorteada = randint(0,len(lista)-1)
    return posicao_sorteada

def embaralhar_palavra(palavra_escolhida: str):
    '''
    Função que recebe uma palavra como parâmetro, embaralha as letras e retorna a string.
        - Argumentos:
            palavra_escolhida (str) - recebe uma string.
        - Retorna:
            palavra_embaralhada (str) - retorna uma string com caracteres embaralhados baseado na string recebida.
    '''
    conjunto_de_letras = list(palavra_escolhida) #converte uma palavra numa lista de caracteres
    palavra_embaralhada = '' 

    while len(conjunto_de_letras) != 0: #loop que concatena letras do 'conjunto_de_letras' na variável 'palavra_embaralhada' até que não sobre mais letras
        letra_selecionada = randint(0,len(conjunto_de_letras)-1) 

        palavra_embaralhada = palavra_embaralhada + conjunto_de_letras[letra_selecionada]
        conjunto_de_letras.pop(letra_selecionada)

    return palavra_embaralhada

def jogar_turno(string_analisada: str):
    '''
    Função que recebe uma string e compara com uma 'entrada de usuário' retornando um valor booleado.
        - Argumentos:
            string_analisada (str) - recebe uma string.
        - Retorna:
            (bool) - retorna um valor True ou False dependendo do resultado da comparação.
    '''
    tentativa = input('Descobriu a palavra embaralhada? Digite sua tentativa: ')
    
    if tentativa == string_analisada:
        return True
    else:
        return False
