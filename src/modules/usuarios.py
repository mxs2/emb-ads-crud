import json
import os

class Usuarios:
    def __init__(self):
        self.usersData = os.path.join(os.path.dirname(__file__), './db/usuariosData.json')
        if not os.path.exists(self.usersData):
            with open(self.usersData, 'w') as userDataArquivo:
                json.dump([], userDataArquivo, indent=4)

    def carregar(self):
        with open(self.usersData, 'r') as usersDataArquivo:
            return json.load(usersDataArquivo)

    def adicionar(self, nome, idade, genero, contato, cpf):
        users = self.carregar()
        users.append({'nome': nome, 'idade': idade, 'genero': genero, 'contato': contato, 'cpf': cpf})
        with open(self.usersData, 'w') as userDataArquivo:
            json.dump(users, userDataArquivo, indent=4, ensure_ascii=False)
        print("Usuário cadastrado com sucesso!")

    def listar(self):
        users = self.carregar()
        if users:
            for user in users:
                print(f"Nome: {user['nome']}, Idade: {user['idade']}, Gênero: {user['genero']}, Contato: {user['contato']}, CPF: {user['cpf']}")
        else:
            print("Nenhum usuário cadastrado.")

    def buscar(self, cpf):
        users = self.carregar()
        for user in users:
            if user['cpf'] == cpf:
                print(f"Usuário encontrado: {user}")
                return
        print("Usuário não encontrado.")

    def atualizar(self, cpf, nome, idade, genero, contato):
        users = self.carregar()
        for user in users:
            if user['cpf'] == cpf:
                user['nome'] = nome
                user['idade'] = idade
                user['genero'] = genero
                user['contato'] = contato
                with open(self.usersData, 'w') as userDataArquivo:
                    json.dump(users, userDataArquivo, indent=4, ensure_ascii=False)
                print("Usuário atualizado com sucesso.")
                return
        print("Usuário não encontrado.")
    
    def remover(self, cpf):
        users = self.carregar()
        for user in users:
            if user['cpf'] == cpf:
                users.remove(user)
                with open(self.usersData, 'w') as userDataArquivo:
                    json.dump(users, userDataArquivo, indent=4, ensure_ascii=False)
                print("Usuário removido com sucesso.")
                return
        print("Usuário não encontrado.")
