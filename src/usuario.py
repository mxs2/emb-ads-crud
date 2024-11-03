import json
import os

usersData = os.path.join(os.path.dirname(__file__), 'usuariosData.json')


def carregar_user():
    if not os.path.exists(usersData):
        with open(usersData, 'w') as userDataArquivo:
            json.dump([], userDataArquivo, indent=4)

def adicionar_user(nome, idade, genero, contato, cpf):
    usuarios = carregar_user()

    usuarios.append({'nome': nome, 'idade': idade, 'genero': genero, 'contato': contato, 'cpf': cpf})

    with open(usersData, 'w') as userDataArquivo:
        json.dump(usuarios, userDataArquivo, indent=4, ensure_ascii=False)
    print("Você foi cadastrado com sucesso :)")

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
    #nome,idade, genero e contato
        menu_user()
        op= input("Escolha uma opção: ")
    
        if op == "1":
            nome=input("Digite o seu nome: ")          
            idade=input("Digite sua idade: ")      
            genero=input("Digite seu gênero: ")
            contato=input("Digite seu telefone: ")
            cpf= input("Digite seu CPF: ")
            adicionar_user(nome,idade,genero,contato,cpf)
        
if __name__ == "__main__":
    main()