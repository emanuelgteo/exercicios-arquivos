# EXERCÍCIO DE FIXAÇÃO
# Exercício de fixação 3: Crie um programa que escreva um arquivo chamado "alunos.txt" contendo informações de alunos (um aluno por linha, separado por vírgulas - nome, idade, nota) conforme a lista abaixo. Dica: se quiser, pesquise sobre a função “map” em Python. Ela serve para substituir o “for” em alguns casos.

alunos = [

    ("João", 18, 9.5),

    ("Maria", 19, 8.7),

    ("Pedro", 20, 7.2),

    ("Ana", 18, 9.0),

    ("Carlos", 19, 8.5)

]

with open('alunos.txt', 'w', encoding='utf-8') as arquivo:
    for aluno in alunos:

        arquivo.write(", ".join(map(str, aluno)) + '\n')

        # Explicando os comandos dentro de for:

        # Inicialmente, itera-se a função str() para cada tupla dentro de alunos, o que dá origem a uma string a cada nova iteração do map.
        # Exemplo: alunos[0] = ("João", 18, 9.5)
        # O map vai fazer: 
        # str("João") = "João"
        # str(18) = "18"
        # str(9.5) = "9.5"
        # Em seguida, o .join vai pegar esses iteradores e conectá-los pela string conectora, que foi definida como ", "
        #Então, para cada elemento de alunos, isso ocorrerá e uma linha será escrita no arquivo txt