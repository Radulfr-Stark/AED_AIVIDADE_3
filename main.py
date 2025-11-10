from modulos import *

lista = []

while len(lista) < 7:
    palavra = solicita_palavra()
    if palavra != '': 
        lista.append(palavra)

contador_turnos = 7

palavra_sorteada = lista[randint(0,len(lista)-1)]
palavra_embaralhada = embaralhar_palavra(palavra_sorteada)

while palavra_sorteada == palavra_embaralhada: #loop que garante que a palavra embaralhada não será igual à sua grafia correta
    palavra_embaralhada = embaralhar_palavra(palavra_sorteada)



# print(palavra_embaralhada)
# print(lista)
# print(palavra_sorteada)

