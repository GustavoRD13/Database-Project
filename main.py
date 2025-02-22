from Database import (conectar_banco, salvar_personagem_no_banco, criar_tabela_personagem,
                      Criar_personagem, Consultar_Personagem, Remover_Personagem, Alterar_personagem)
from Character import criar_instancia_personagem
from Utility import espacamento, tratar_nome, validar_raca

def criar_personagem():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        c_nome = tratar_nome()
        raca = validar_raca()
        personagem = criar_instancia_personagem(c_nome, raca)  # Do módulo personagens
        salvar_personagem_no_banco(cursor, personagem)        # Do módulo database
        conexao.commit()
        print(f"O personagem {personagem.nome} foi criado com sucesso!")
    finally:
        cursor.close()
        conexao.close()
        """Podemos dividir a função criar_personagem() em duas partes:
        Criação lógica do personagem (em personagens.py).
        Persistência no banco de dados (em database.py)."""

def main():
    while True:
        criar_tabela_personagem()
        espacamento("Menu principal")
        print("1 - Criação de personagens")
        print("2 - Alteração de personagens")
        print("3 - Remoção de Personagem")
        print("4 - Consulta de Personagens")
        print("5 - Sair\n")

        try:
            opcao = int(input("Selecione a opção desejada (1-5): ").strip())
            if opcao == 1:
                Criar_personagem()
            elif opcao == 2:
                Alterar_personagem()
            elif opcao == 3:
                Remover_Personagem()
            elif opcao == 4:
                Consultar_Personagem()
            elif opcao == 5:
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida. Escolha entre 1 e 5.\n")
        except ValueError:
            print("Entrada inválida. Escolha entre 1 e 5.\n")

if __name__ == "__main__":
    main()
