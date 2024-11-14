import json
import os


class Cor:
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    RESET = "\033[0m"


class Usuarios:
    def __init__(self):
        self.usersData = os.path.join(
            os.path.dirname(__file__), "./db/usuariosData.json"
        )
        if not os.path.exists(self.usersData):
            with open(self.usersData, "w") as userDataArquivo:
                json.dump([], userDataArquivo, indent=4)

    def carregar(self):
        try:
            with open(self.usersData, "r") as usersDataArquivo:
                return json.load(usersDataArquivo)
        except json.JSONDecodeError:
            print(
                Cor.VERMELHO
                + "Erro ao carregar dados: arquivo JSON inválido."
                + Cor.RESET
            )
            return []

    def salvar(self, users):
        with open(self.usersData, "w") as userDataArquivo:
            json.dump(users, userDataArquivo, indent=4, ensure_ascii=False)

    def adicionar(self, nome, idade, genero, contato, cpf):
        users = self.carregar()
        users.append(
            {
                "nome": nome,
                "idade": idade,
                "genero": genero,
                "contato": contato,
                "cpf": cpf,
            }
        )
        self.salvar(users)
        print(Cor.VERDE + "✅ Usuário cadastrado com sucesso!" + Cor.RESET)

    def listar(self):
        users = self.carregar()
        if users:
            print(Cor.AZUL + "Lista de Usuários Cadastrados:" + Cor.RESET)
            for user in users:
                print(
                    f"Nome: {user['nome']}, Idade: {user['idade']}, Gênero: {user['genero']}, "
                    f"Contato: {user['contato']}, CPF: {user['cpf']}"
                )
        else:
            print(Cor.AMARELO + "⚠️ Nenhum usuário cadastrado." + Cor.RESET)

    def buscar(self, cpf):
        users = self.carregar()
        for user in users:
            if user["cpf"] == cpf:
                print(Cor.VERDE + "✅ Usuário encontrado:" + Cor.RESET)
                print(
                    f"Nome: {user['nome']}, Idade: {user['idade']}, Gênero: {user['genero']}, "
                    f"Contato: {user['contato']}, CPF: {user['cpf']}"
                )
                return
        print(Cor.VERMELHO + "❌ Usuário não encontrado." + Cor.RESET)

    def atualizar(self, cpf, nome, idade, genero, contato):
        users = self.carregar()
        for user in users:
            if user["cpf"] == cpf:
                user["nome"] = nome
                user["idade"] = idade
                user["genero"] = genero
                user["contato"] = contato
                self.salvar(users)
                print(Cor.VERDE + "✅ Usuário atualizado com sucesso." + Cor.RESET)
                return
        print(Cor.VERMELHO + "❌ Usuário não encontrado." + Cor.RESET)

    def remover(self, cpf):
        users = self.carregar()
        for user in users:
            if user["cpf"] == cpf:
                users.remove(user)
                self.salvar(users)
                print(Cor.VERDE + "✅ Usuário removido com sucesso." + Cor.RESET)
                return
        print(Cor.VERMELHO + "❌ Usuário não encontrado." + Cor.RESET)
