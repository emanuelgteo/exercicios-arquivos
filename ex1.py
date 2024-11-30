# Exercício 1
# Crie um dicionário com o nome e a profissão de duas pessoas e adicione uma terceira pessoa com nome e profissão. Salve o resultado em um arquivo JSON.

import json

profissoes = {
    "José": "Atleta",
    "Jennifer": "Cantora" 
}

print(profissoes)

profissoes["Sérgio"] = "Líder de Escoteiro"

print(profissoes)

with open('profissoes.json', 'w', encoding='utf-8') as arquivo:
    json.dump(profissoes, arquivo, ensure_ascii=False)

