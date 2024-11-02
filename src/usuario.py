import json
import os

usersData = os.path.join(os.path.dirname(__file__), 'usuariosData.json')

def menu_user():
    print("\nMENU USUÁRIOS:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. LISTAR UM USUÁRIO")
    print("6. VOLTAR AO MENU ANTERIOR")
    

def main(): 
    while True:
        opcao_inicial = int(input("Escolha uma opção:\n>>>"))
        match opcao_inicial:
            case(1):
                print("Op 1")

if __name__ == "__main__":
    main()