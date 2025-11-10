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
