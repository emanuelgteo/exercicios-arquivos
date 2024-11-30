# Exercício 5
# Modifique o código do exercício 4 para que salve, dentro de um único arquivo, as duas listas. Depois, abra novamente o arquivo pickle que salvou e mostre na tela o seu conteúdo.

import random
import pickle

numeros = []
pares = []

tamanho = int(input('Você quer uma lista com quantos números de 1 a 10? '))
for i in range(tamanho):
    num = random.randrange(1,11)
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)

with open('lista_num.pickle', 'wb') as arquivo:
    pickle.dump([numeros,pares], arquivo)

with open('lista_num.pickle', 'rb') as arquivo:
    num_lidos, num_pares_lidos = pickle.load(arquivo)

print(num_lidos)
print(num_pares_lidos)