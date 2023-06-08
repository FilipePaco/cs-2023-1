class Contato:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, email):
        contato = Contato(nome, email)
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def buscar_contato(self, nome_ou_email):
        for contato in self.contatos:
            if contato.nome == nome_ou_email or contato.email == nome_ou_email:
                return contato
        return None

    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print("Contato excluído com sucesso!")
                return
        print("Contato não encontrado.")

    def listar_contatos(self):
        if len(self.contatos) == 0:
            print("Não há contatos na agenda.")
        else:
            print("Contatos na agenda:")
            for contato in self.contatos:
                print("Nome:", contato.nome)
                print("Email:", contato.email)
                print("-----")


# Exemplo de uso
agenda = Agenda()

while True:
    print("Escolha uma opção:")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Excluir contato")
    print("4. Listar contatos")
    print("0. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        email = input("Digite o email do contato: ")
        agenda.adicionar_contato(nome, email)
    elif opcao == "2":
        nome_ou_email = input("Digite o nome ou email do contato: ")
        contato = agenda.buscar_contato(nome_ou_email)
        if contato is not None:
            print("Contato encontrado:")
            print("Nome:", contato.nome)
            print("Email:", contato.email)
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        nome = input("Digite o nome do contato a ser excluído: ")
        agenda.excluir_contato(nome)
    elif opcao == "4":
        agenda.listar_contatos()
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Digite um número válido.")

    print()  # Nova linha para separar as opções
