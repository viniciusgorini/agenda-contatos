# agenda.py

contatos = []


def cadastrar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)
    print("Contato cadastrado com sucesso!")


def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    for indice, contato in enumerate(contatos, start=1):
        print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}")


def buscar_contato():
    termo = input("Digite o nome (ou parte dele) para buscar: ")
    encontrou = False

    for contato in contatos:
        if termo.lower() in contato["nome"].lower():
            print(
                f"{contato['nome']} - "
                f"{contato['telefone']} - {contato['email']}"
            )
            encontrou = True

    if not encontrou:
        print("Nenhum contato encontrado.")


def remover_contato():
    pass


while True:
    print("\n=== Agenda de Contatos ===")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        print("Até logo!")
        break
    else:
        print("Opção inválida.")
