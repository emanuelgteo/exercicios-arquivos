# EXERCÍCIO DE FIXAÇÃO
# Exercício de fixação 2: Crie um programa que leia o arquivo “números.txt” do exercício anterior, e calcule a soma desses números.

soma = 0
with open('números.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha)
        num = int(linha)
        print(num)
        soma += num

print(soma)