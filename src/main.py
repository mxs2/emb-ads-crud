from modules.usuarios import Usuarios
from modules.animais import Animais
from modules.adocoes import Adocoes
from time import sleep


class cor:
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIANO = "\033[96m"
    RESET = "\033[0m"


def menu_inicial():
    print(cor.AZUL + "=" * 50 + cor.RESET)
    print(cor.VERDE + "         Sistema de Adoção Animal         " + cor.RESET)
    print(cor.AZUL + "=" * 50 + cor.RESET)
    print("1 - Módulo Usuários")
    print("2 - Módulo Animais")
    print("3 - Módulo Adoções")
    print("4 - Sair")
    print(cor.AZUL + "=" * 50 + cor.RESET)


def main():
    usuarios = Usuarios()
    animais = Animais()
    adocoes = Adocoes()

    while True:
        menu_inicial()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(cor.CIANO + "\nMódulo Usuários\n" + cor.RESET)
            print(
                "1 - Adicionar Usuário\n2 - Listar Usuários\n3 - Buscar Usuário\n"
                "4 - Atualizar Usuário\n5 - Remover Usuário\n6 - Voltar ao Menu"
            )
            opcao_user = input("Escolha uma opção: ")
            if opcao_user == "1":
                nome = input("Nome: ")
                idade = input("Idade: ")
                genero = input("Gênero: ")
                contato = input("Contato: ")
                cpf = input("CPF: ")
                usuarios.adicionar(nome, idade, genero, contato, cpf)
                print(cor.VERDE + "Usuário adicionado com sucesso!" + cor.RESET)
            elif opcao_user == "2":
                usuarios.listar()
            elif opcao_user == "3":
                cpf = input("CPF: ")
                usuarios.buscar(cpf)
            elif opcao_user == "4":
                cpf = input("CPF: ")
                nome = input("Nome: ")
                idade = input("Idade: ")
                genero = input("Gênero: ")
                contato = input("Contato: ")
                usuarios.atualizar(cpf, nome, idade, genero, contato)
            elif opcao_user == "5":
                cpf = input("CPF: ")
                usuarios.remover(cpf)
            elif opcao_user == "6":
                continue

        elif opcao == "2":
            print(cor.CIANO + "\nMódulo Animais\n" + cor.RESET)
            print(
                "1 - Adicionar Animal\n2 - Listar Animais\n3 - Buscar Animal\n"
                "4 - Atualizar Animal\n5 - Remover Animal\n6 - Voltar ao Menu"
            )
            opcao_animal = input("Escolha uma opção: ")
            if opcao_animal == "1":
                nome = input("Nome do pet: ")
                especie = input("Espécie do pet: ")
                genero = input("Gênero do pet: ")
                raca = input("Raça do pet: ")
                idade = input("Idade do pet: ")
                animais.adicionar(nome, especie, genero, raca, idade)
                print(cor.VERDE + "Animal adicionado com sucesso!" + cor.RESET)
            elif opcao_animal == "2":
                animais.listar()
            elif opcao_animal == "3":
                nome = input("Nome do pet: ")
                animais.buscar(nome)
            elif opcao_animal == "4":
                nome = input("Nome do pet: ")
                especie = input("Espécie do pet: ")
                genero = input("Gênero do pet: ")
                raca = input("Raça do pet: ")
                idade = input("Idade do pet: ")
                animais.atualizar(nome, especie, genero, raca, idade)
            elif opcao_animal == "5":
                nome = input("Nome do pet: ")
                animais.remover(nome)
            elif opcao_animal == "6":
                continue

        elif opcao == "3":
            print(cor.CIANO + "\nMódulo Adoções\n" + cor.RESET)
            print(
                "1 - Adicionar Pedido de Adoção\n2 - Listar Pedidos de Adoção\n3 - Buscar Pedido\n"
                "4 - Atualizar Pedido\n5 - Remover Pedido\n6 - Voltar ao Menu"
            )
            opcao_pedido = input("Escolha uma opção: ")
            if opcao_pedido == "1":
                cpf = input("CPF: ")
                nome = input("Nome: ")
                idade = input("Idade: ")
                animalType = input("Animal desejado: ")
                raca = input("Raça: ")
                genero = input("Gênero: ")
                adocoes.adicionar(cpf, nome, idade, animalType, raca, genero)
                print(
                    cor.VERDE + "Pedido de adoção adicionado com sucesso!" + cor.RESET
                )
            elif opcao_pedido == "2":
                adocoes.listar()
            elif opcao_pedido == "3":
                cpf = input("CPF: ")
                adocoes.buscar(cpf)
            elif opcao_pedido == "4":
                cpf = input("CPF: ")
                nome = input("Nome: ")
                idade = input("Idade: ")
                animalType = input("Animal desejado: ")
                raca = input("Raça: ")
                genero = input("Gênero: ")
                adocoes.atualizar(cpf, nome, idade, animalType, raca, genero)
            elif opcao_pedido == "5":
                cpf = input("CPF: ")
                adocoes.remover(cpf)
            elif opcao_pedido == "6":
                continue

        elif opcao == "4":
            print(cor.VERMELHO + "Saindo do sistema... Até logo!" + cor.RESET)
            sleep(2)
            break

        else:
            print(cor.VERMELHO + "Opção inválida, tente novamente." + cor.RESET)
            sleep(1)


if __name__ == "__main__":
    main()
