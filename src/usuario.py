import json
import os

usersData = os.path.join(os.path.dirname(__file__), 'usuariosData.json')
if not os.path.exists(usersData):
    with open(usersData, 'w') as userDataArquivo:
        json.dump({}, userDataArquivo, indent=4)

def carregar_user():
    with open(usersData, 'r') as usersDataArquivo:
        return json.load(userDataArquivo)


def adicionar_user(nome, idade, genero, contato, cpf):
    users = carregar_user()
    if users is None:
        users = []
    
    users.append({'nome': nome, 'idade': idade, 'genero': genero, 'contato': contato, 'cpf': cpf})

    with open(usersData, 'w') as userDataArquivo:
        json.dump(users, userDataArquivo, indent=4, ensure_ascii=False)
    print("Você foi cadastrado com sucesso :)")
    
    
def listar_user():
    users = carregar_user()

    if users:
        print("=" *50)
        print("Lista de usuários: ")
        print("-" *50)
        for user in users:
            print("*" *50)
            print(f"Nome: {user['nome']}, Idade: {user['idade']}, Gênero: {user['genero']}, Telefone:{user['telefone']}, CPF:{user['cpf']}")
            print("*" *50)
            print("=" *50)
    else:
        print("Nenhum usuário cadastrado")

def atualizar_User(nome_antigo, novo_nome, nova_idade, novo_genero, novo_contato, novo_cpf):
    users = carregar_user()

    for user in users:
        if user['nome'] == nome_antigo:
            user['nome'] == novo_nome
            user['idade'] == nova_idade
            user['genero'] == novo_genero
            user['contato'] == novo_contato
            user['cpf'] == novo_cpf
            break
    with open(usersData, 'w') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)
    print("USUÁRIO ATUALIZADO !!!")

def exluir_User(nome):
    users = carregar_user()

    for user in users:  
        if user['nome'] == nome:
            users.remove(user)

    with open(usersData, 'w') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)
    print("USUÁRIO DELETADO !!!")

def listar_User(nome):
    users = carregar_user()

    for user in users:
        if user['nome'] == nome:
            print(f"NOME: {user['nome']}, IDADE: {user['idade']}, GENERO: {user['genero']}, CONTATO: {user['contato']}, CPF: {user['cpf']}")
    
    else:
        print("NENHUM USUÁRIO ENCONTRADO !!!")

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
        
        menu_user()
        op= input("Escolha uma opção: ")
    
        if op == "1":
            nome=input("Digite o seu nome: ")          
            idade=input("Digite sua idade: ")      
            genero=input("Digite seu gênero: ")
            contato=input("Digite seu telefone: ")
            cpf= input("Digite seu CPF: ")
            adicionar_user(nome,idade,genero,contato,cpf)
            
        elif op == "2":
            listar_user()         
            #TÁ DANDO ERRO 
            
            
            
if __name__ == "__main__":
    main()