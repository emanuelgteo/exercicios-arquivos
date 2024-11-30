# Exercício 4
# Crie uma lista com números de 1 a 10 e, em seguida, crie uma segunda lista contendo somente os números pares. Salve somente a lista dos números pares em um arquivo pickle. Depois, abra novamente o arquivo pickle que salvou e mostre na tela o seu conteúdo.

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

print(numeros)

with open('lista_num.pickle', 'wb') as arquivo:
    pickle.dump(pares, arquivo)

with open('lista_num.pickle', 'rb') as arquivo:
    conteudo = pickle.load(arquivo)

print(conteudo)