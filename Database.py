import sqlite3 as conector
from Utility import espacamento, tratar_nome, validar_raca, perguntar_sim_nao, tratar_id
from Character import Humano, Orc, Elf
DB_NAME = 'RPGdata.db'

def conectar_banco():
    conexao = conector.connect(DB_NAME)
    conexao.execute("PRAGMA foreign_keys = on")
    return conexao

def criar_tabela_personagem():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        comando_c1 = '''CREATE TABLE IF NOT EXISTS Personagem (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        raca TEXT NOT NULL,
                        vida INTEGER NOT NULL,
                        ataque INTEGER NOT NULL,
                        defesa INTEGER NOT NULL,
                        velocidade INTEGER NOT NULL,
                        inteligencia INTEGER NOT NULL);'''

        cursor.execute(comando_c1)
        conexao.commit()
    finally:
        cursor.close()
        conexao.close()

def salvar_personagem_no_banco(cursor, personagem):
    cursor.execute('''INSERT INTO Personagem (nome, raca, vida, ataque, defesa, velocidade, inteligencia)
                       VALUES (?, ?, ?, ?, ?, ?, ?);''',
                   (personagem.nome, personagem.raca, personagem.vida,
                    personagem.ataque, personagem.defesa,
                    personagem.velocidade, personagem.inteligencia))

def Criar_personagem():
    conexao = conector.connect(DB_NAME)
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()
    try:
        while True:
            espacamento("Criação de personagem")
            c_nome = tratar_nome()
            raca = validar_raca()
            personagem = {"Humano": Humano, "Orc": Orc, "Elf": Elf}[raca](c_nome)

            cursor.execute('''INSERT INTO Personagem (nome, raca, vida, ataque, defesa, velocidade, inteligencia)
                                           VALUES (?, ?, ?, ?, ?, ?, ?);''',
                           (personagem.nome, personagem.raca, personagem.vida,
                            personagem.ataque, personagem.defesa,
                            personagem.velocidade, personagem.inteligencia))
            conexao.commit()
            print(f"O personagem {personagem.nome} foi criado com sucesso!")

            if perguntar_sim_nao("Deseja criar outro personagem? (S/N): ") == "N":
                break
    finally:
        cursor.close()
        conexao.close()

def Alterar_personagem():
    conexao = conector.connect(DB_NAME)
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()
    try:
        while True:
            espacamento("Alterar personagem")
            print("[1] - Alterar nome\n"
                  "[2] - Alterar raça\n"
                  "[3] - Sair\n")

            opcao = input("Escolha a opção: ").strip()

            if opcao == "1":
                # Alterar apenas o nome
                u_id = tratar_id(cursor)
                u_nome = tratar_nome()

                cursor.execute("UPDATE Personagem SET nome = ? WHERE id = ?;", (u_nome, u_id))
                conexao.commit()
                print(f"Nome alterado com sucesso!\nNovo nome: {u_nome}\n")

            elif opcao == "2":
                # Alterar raça e atualizar atributos
                u_id = tratar_id(cursor)
                u_raca = validar_raca()

                # Recalcular atributos com base na nova raça
                personagem = {"Humano": Humano, "Orc": Orc, "Elf": Elf}[u_raca]("Temporario")

                # Atualizar a raça e os atributos no banco de dados
                cursor.execute('''
                    UPDATE Personagem 
                    SET raca = ?, vida = ?, ataque = ?, defesa = ?, velocidade = ?, inteligencia = ?
                    WHERE id = ?;
                ''', (personagem.raca, personagem.vida, personagem.ataque, personagem.defesa, personagem.velocidade, personagem.inteligencia, u_id))

                conexao.commit()
                print(f"Raça alterada com sucesso! Atributos atualizados para a nova raça {u_raca}.\n")
                print(personagem)  # Exibe os novos atributos do personagem

            elif opcao == "3":
                break
            else:
                print("Opção inexistente, tente novamente!\n")

    except conector.DatabaseError as err:
        print(f"Erro no banco de dados: {err}")
    except ValueError as err:
        print(f"Erro de valor: {err}")

    finally:
        cursor.close()
        conexao.close()

def Remover_Personagem():
    conexao = conector.connect(DB_NAME)
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()
    try:
        while True:
            print("[1] - Remover Personagem \n"
                  "[2] - Sair\n")

            opcao = input("Escolha a opção desejada: ").strip()
            if opcao == "1":
                d_id = tratar_id(cursor)
                comando_delete = '''DELETE FROM Personagem WHERE id = ?;'''
                cursor.execute(comando_delete, (d_id,))
                conexao.commit()
                print("\n" f"Personagem com o id {d_id} foi removido da lista\n")

            elif opcao == "2":
                break
            else:
                print("Opção inexistente, tente novamente!")
    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        cursor.close()
        conexao.close()

def Consultar_Personagem():
    conexao = conector.connect(DB_NAME)
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()
    try:
        while True:
            print("[1] - Lista de personagem \n"
                  "[2] - Sair\n")

            opcao = input("Escolha a opção desejada: ""\n").strip()
            if opcao == "1":
                r_personagem = '''SELECT id, nome, raca, vida, ataque, defesa, velocidade, inteligencia
                                  FROM Personagem ORDER BY id;'''
                cursor.execute(r_personagem)
                data_personagem = cursor.fetchall()
                for data in data_personagem:
                    print(f"ID: {data[0]} | Nome: {data[1]} | Raça: {data[2]}\n"
                          f"Vida: {data[3]} | Ataque: {data[4]} | Defesa: {data[5]}\n"
                          f"Velocidade: {data[6]} | Inteligência: {data[7]}\n")

            elif opcao == "2":
                break
            else:
                print("Opção inexistente, tente novamente!\n")
    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        cursor.close()
        conexao.close()