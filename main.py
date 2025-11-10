from modulos import *

lista = preencher_lista(3)
palavra_sorteada = lista[sortear_posicao(lista)]
palavra_embaralhada = embaralhar_palavra(palavra_sorteada)

while palavra_sorteada == palavra_embaralhada: #loop que garante que a palavra embaralhada não será igual à sua grafia correta
    palavra_embaralhada = embaralhar_palavra(palavra_sorteada)

condador_turnos = 1

while condador_turnos <= 7:
    print(f'\nComeçando o {condador_turnos}º turno...\n\nDescubra/desembaralhe a palavra [{palavra_embaralhada}]')
    resultado = jogar_turno(palavra_sorteada)
    condador_turnos += 1

    if resultado == True:
        break
    else:
        print(f'Negativo, sua opção não desembaralhou: {palavra_embaralhada}\n\nUma dica: use maiúsculas!\n')
        continue



# print(palavra_embaralhada)
print('Descobriu a palavra sorteada ->', palavra_sorteada)
# print(palavra_sorteada)

