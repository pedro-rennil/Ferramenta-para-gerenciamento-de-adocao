import json
import os

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")

def carregar_dados():
    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_dados(dados):
    with open(DATA_FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4)


def gerar_id_unico(dados):
    if not dados:
        return 1  
    else:
        maior_id = max(animal["id"] for animal in dados)
        return maior_id + 1

def adicionar_animal(nome, especie, raca, idade, personalidade, situacao_saude):
    dados = carregar_dados()
    novo_id = gerar_id_unico(dados) 
    novo_animal = {
        "id": novo_id,
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "personalidade": personalidade,
        "situacao_saude": situacao_saude  
    }
    dados.append(novo_animal)
    salvar_dados(dados)
    print(f"Animal adicionado com sucesso! ID: {novo_id}")

def buscar_animal(nome):
    dados = carregar_dados()
    resultados = [animal for animal in dados if animal["nome"].lower() == nome.lower()]
    if resultados:
        for animal in resultados:
            print(f"ID: {animal['id']} - Nome: {animal['nome']}, Espécie: {animal['especie']}, Raça: {animal['raca']}, Idade: {animal['idade']}, Personalidade: {animal['personalidade']}, Saúde: {animal['situacao_saude']}")
    else:
        print(f"Animal com nome '{nome}' não encontrado.")


def listar_animais():
    dados = carregar_dados()
    if not dados: 
        print("Nenhum animal encontrado.")
        return
    for animal in dados:
        print(f"ID: {animal['id']} - Nome: {animal['nome']}, Espécie: {animal['especie']}, Raça: {animal['raca']}, Idade: {animal['idade']}, Personalidade: {animal['personalidade']}, Saúde: {animal['situacao_saude']}")

def atualizar_animal(id, novo_nome, nova_especie, nova_raca, nova_idade, nova_personalidade, nova_situacao_saude):
    dados = carregar_dados()
    for animal in dados:
        if  animal["id"] == id:
            animal["nome"] = novo_nome
            animal["especie"] = nova_especie
            animal["raca"] = nova_raca
            animal["idade"] = nova_idade
            animal["personalidade"] = nova_personalidade
            animal["situacao_saude"] = nova_situacao_saude  
            salvar_dados(dados)
            print("Animal atualizado com sucesso!")
            return
    print("Animal não encontrado.")

def deletar_animal(id):
    dados = carregar_dados()
    dados = [animal for animal in dados if animal["id"] != id]
    salvar_dados(dados)
    print("Animal removido com sucesso!")