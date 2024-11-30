# EXERCÍCIO DE FIXAÇÃO
# Exercício de fixação 4: Crie um programa que leia o arquivo "alunos.txt" do exercício anterior. Em seguida, calcule a média das notas dos alunos e exiba na saída padrão. Dica: se quiser, pesquise sobre o método “split” em Python. Ele serve para dividir a string em strings menores.
soma = 0
i = 0
with open('alunos.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        separar_string = linha.split(', ')
        nota = separar_string[2]
        soma += float(nota)
        i += 1
media = soma/i
print(media)
    