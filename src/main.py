from modules.usuarios import Usuarios
from modules.animais import Animais
from modules.adocoes import Adocoes

def menu_inicial():
    print("Sistema de Adoção")
    print("1 - Módulo Usuários")
    print("2 - Módulo Animais")
    print("3 - Módulo Adoção")
    print("4 - Sair")

def main():
    usuarios = Usuarios()
    animais = Animais()
    adocoes = Adocoes()
    
    while True:
        menu_inicial()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("\n1 - Adicionar Usuário\n2 - Listar Usuários")
            opcao_user = input("Escolha uma opção: ")
            if opcao_user == "1":
                nome = input("Nome: ")
                idade = input("Idade: ")
                genero = input("Gênero: ")
                contato = input("Contato: ")
                cpf = input("CPF: ")
                usuarios.adicionar(nome, idade, genero, contato, cpf)
            elif opcao_user == "2":
                usuarios.listar()
        elif opcao == "2":
            print("\n1 - Adicionar Animal\n2 - Listar Animais")
            opcao_animal = input("Escolha uma opção: ")
            if opcao_animal == "1":
                nome = input("Nome do pet: ")
                especie = input("Espécie do pet: ")
                genero = input("Gênero do pet: ")
                raca = input("Raça do pet: ")
                idade = input("Idade do pet: ")
                animais.adicionar(nome, especie, genero, raca, idade)
            elif opcao_animal == "2":
                animais.listar()
        elif opcao == "3":
            print("\n1 - Adicionar Pedido de Adoção\n2 - Listar Pedidos de Adoção")
            opcao_pedido = input("Escolha uma opção: ")
            if opcao_pedido == "1":
                cpf = input("CPF: ")
                nome = input("Nome: ")
                idade = input("Idade: ")
                animalType = input("Animal desejado: ")
                raca = input("Raça: ")
                genero = input("Gênero: ")
                adocoes.adicionar(cpf, nome, idade, animalType, raca, genero)
            elif opcao_pedido == "2":
                adocoes.listar()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
