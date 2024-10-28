import json
import os

usersData = os.path.join(os.path.dirname(__file__), 'usuariosData.json')

def menu_inicial():
    print("ADOTE PET")
    print("1 - MÓDULO DO USUÁRIOS ")
    print("2 - ADOTE UM PET")
    print("3 - MÓDULO DO ANIMAL")
    print("4 - SAIR ")

def menu_user():
    print("\nMENU USUÁRIOS:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. LISTAR UM USUÁRIO")
    print("6. VOLTAR AO MENU ANTERIOR")

def menu_adotar():
    print("\nMENU PEDIDOS DE ADOÇÃO:")
    print("1. CRIAR PEDIDO DE ADOÇÃO")
    print("2. LISTAR PEDIDOS DE ADOÇÃO")
    print("3. ATUALIZAR PEDIDO DE ADOÇÃO")
    print("4. EXCLUIR PEDIDO DE ADOÇÃO")
    print("5. LISTAR UM PEDIDO DE ADOÇÃO")
    print("6. VOLTAR AO MENU ANTERIOR")

def menu_animais():
    print("\nMENU ANIMAIS PARA ADOÇÃO:")
    print("1. ADICIONAR ANIMAL")
    print("2. LISTAR ANIMAIS")
    print("3. ATUALIZAR ANIMAL")
    print("4. EXCLUIR ANIMAL")
    print("5. LISTAR UM ANIMAL")
    print("6. VOLTAR AO MENU ANTERIOR")

def main(): 
    while True:
        menu_inicial()
        opcao_inicial = int(input("Escolha uma opção:\n>>>"))
        match opcao_inicial:
            case(1):
                print("Op 1")

if __name__ == "__main__":
    main()