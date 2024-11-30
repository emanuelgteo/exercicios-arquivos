# Exercício 2
# Crie um código que peça para o usuário digitar uma frase. Salve o resultado em uma arquivo de texto. Depois, abra este arquivo de texto que salvou e mostre o resultado na tela.

mensagem = input('Digite uma frase: ')

with open('mensagem.txt', 'w') as arquivo:
    arquivo.write(mensagem)

with open('mensagem.txt', 'r') as arquivo:
    print(arquivo.read())