from modulos import *

print('''
##################################################
----Bem vindo ao jogo DESEMBARALHE O SORTEADO!----
##################################################
    O jogo vai preencher uma lista, com palavras
que você escolher e então sortear uma delas, você 
terá que descobri-la antes que seus turnos acabem!
      
----------------------------------------BOA SORTE!
''')

lista = preencher_lista(10)
print('Mínimo da lista já foi preenchido.')

continuar = input('Digite "SIM" e pressione [ENTER] se quiser inserir mais palavras para o sorterio: ').strip().upper()
while continuar == 'SIM':
    lista = preencher_lista(1)
    continuar = input('Digite "SIM" e pressione [ENTER] se quiser inserir mais palavras para o sorterio: ').strip().upper()

palavra_sorteada = lista[sortear_posicao(lista)]
palavra_embaralhada = embaralhar_palavra(palavra_sorteada)

while palavra_sorteada == palavra_embaralhada: #loop que garante que a palavra embaralhada não será igual à sua grafia correta
    palavra_embaralhada = embaralhar_palavra(palavra_sorteada)

contador_turnos = 1
resultado_turno = False

while contador_turnos <= 7:
    print(f'\nComeçando o {contador_turnos}º turno...\n\nDescubra/desembaralhe a palavra [{palavra_embaralhada}]')
    resultado_turno = jogar_turno(palavra_sorteada)
    contador_turnos += 1

    if resultado_turno == True:
        print(f'\nPARABÉNS, você conseguiu identificar a palavra embaralhada [{palavra_embaralhada}] revelando a palavra [{palavra_sorteada}]\n') #mensagem de fim de jogo: VENCEU (GOOD ENDING)
        raise SystemExit
    else:
        print(f'Negativo, sua opção não desembaralhou: {palavra_embaralhada}\n')
        continue

print(f'Infelizmente seus turnos acabaram, mais sorte na próxima vez!') #mensagem de fim de jogo: PERDEU (BAD ENDING)
