import json

# Função para carregar dados do arquivo JSON
def carregar_dados():
    try:
        with open('dados.json', 'r') as f: 
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para salvar dados no arquivo JSON
def salvar_dados(animais):
    with open('dados.json', 'w') as f: 
        json.dump(animais, f, indent=4)