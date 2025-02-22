import re

def espacamento(msg):
    print("-" * 40)
    print(f'{msg:^40}')
    print("-" * 40)

def perguntar_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ["S", "N"]:
            return resposta
        print("Opção inválida. Digite S ou N.")

def tratar_id(cursor):
    while True:
        try:
            u_id = int(input("Digite o ID do personagem: ").strip())
            if verificar_id_existe(cursor, u_id):
                return u_id
            print("Erro: ID não encontrado.")
        except ValueError:
            print("Erro: O ID deve ser um número inteiro.")

def tratar_nome():
    while True:
        nome = input("Digite o nome do Personagem: ").strip().title()
        if re.match("^[A-Za-zÀ-ÖØ-öø-ÿ' ]+$", nome):
            return nome
        else:
            print("O nome deve conter apenas caracteres alfabéticos e espaços.\n")

def validar_raca():
    racas_validas = ["Humano", "Orc", "Elf"]
    while True:
        raca = input("Escolha a raça (Humano, Orc, Elf): ").capitalize()
        if raca in racas_validas:
            return raca
        print("Raça inválida. Tente novamente.")

def verificar_id_existe(cursor, id_personagem):
    cursor.execute("SELECT 1 FROM Personagem WHERE id = ?;", (id_personagem,))
    return cursor.fetchone() is not None
