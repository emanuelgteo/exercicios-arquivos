# Exercício 3
# A partir do exercício 2 e após mostrar o resultado na tela, peça novamente para que o usuário digite uma nova frase. Adicione esta nova frase no mesmo arquivo de texto sem apagar o conteúdo que já estava lá, e mostre o resultado na tela.

mensagem = input('Digite outra frase: ')

with open('mensagem.txt', 'a') as arquivo:
    arquivo.write('\n' + mensagem)

with open('mensagem.txt', 'r') as arquivo:
    print(arquivo.read())