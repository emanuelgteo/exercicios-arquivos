# EXERCÍCIOS DE FIXAÇÃO
# Exercício de fixação 1: Crie um programa que peça ao usuário uma 5 números inteiros. Salve estes números dentro de um arquivo chamado “números.txt”. Cada número deve ocupar uma linha.

i=0
while i < 5:
    try:
        num = int(input('Digite um número inteiro: '))
        with open('números.txt', 'a') as arquivo:
            arquivo.write(str(num)+'\n')
    except:
        print('Valor inválido.')
        i = i-1
    i = i+1
