import json
import os


class Cor:
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    RESET = "\033[0m"


class Adocoes:
    def __init__(self):
        self.adocaoData = os.path.join(
            os.path.dirname(__file__), "./db/adocaoData.json"
        )
        # Cria o arquivo vazio se ele não existir
        if not os.path.exists(self.adocaoData):
            with open(self.adocaoData, "w") as adocaoDataArquivo:
                json.dump({}, adocaoDataArquivo, indent=4)

    def carregar(self):
        # Carrega os dados de adoção e trata possíveis erros de leitura
        try:
            with open(self.adocaoData, "r") as adocaoDataArquivo:
                return json.load(adocaoDataArquivo)
        except json.JSONDecodeError:
            print(
                Cor.VERMELHO
                + "Erro ao carregar dados: arquivo JSON inválido."
                + Cor.RESET
            )
            return {}

    def salvar(self, pedidos):
        # Salva os dados de pedidos de adoção no arquivo
        with open(self.adocaoData, "w") as adocaoDataArquivo:
            json.dump(pedidos, adocaoDataArquivo, indent=4, ensure_ascii=False)

    def adicionar(self, cpf, nome, idade, animalType, raca, genero):
        # Adiciona um pedido de adoção
        pedidos = self.carregar()
        pedidos[cpf] = {
            "nome": nome,
            "idade": idade,
            "animal": animalType,
            "raça": raca,
            "genero": genero,
        }
        self.salvar(pedidos)
        print(Cor.VERDE + "✅ Pedido de adoção adicionado com sucesso!" + Cor.RESET)

    def listar(self):
        # Lista todos os pedidos de adoção
        pedidos = self.carregar()
        if pedidos:
            print(Cor.AZUL + "Lista de Pedidos de Adoção:" + Cor.RESET)
            for cpf, pedido in pedidos.items():
                print(f"CPF: {cpf}, Pedido: {pedido}")
        else:
            print(Cor.AMARELO + "⚠️ Nenhum pedido de adoção encontrado." + Cor.RESET)

    def buscar(self, cpf):
        # Busca um pedido de adoção pelo CPF
        pedidos = self.carregar()
        if cpf in pedidos:
            print(Cor.VERDE + "✅ Pedido de adoção encontrado:" + Cor.RESET)
            print(f"CPF: {cpf}, Pedido: {pedidos[cpf]}")
        else:
            print(Cor.VERMELHO + "❌ Pedido de adoção não encontrado." + Cor.RESET)

    def atualizar(self, cpf, nome, idade, animalType, raca, genero):
        # Atualiza um pedido de adoção pelo CPF
        pedidos = self.carregar()
        if cpf in pedidos:
            pedidos[cpf] = {
                "nome": nome,
                "idade": idade,
                "animal": animalType,
                "raça": raca,
                "genero": genero,
            }
            self.salvar(pedidos)
            print(Cor.VERDE + "✅ Pedido de adoção atualizado com sucesso." + Cor.RESET)
        else:
            print(Cor.VERMELHO + "❌ Pedido de adoção não encontrado." + Cor.RESET)

    def remover(self, cpf):
        # Remove um pedido de adoção pelo CPF
        pedidos = self.carregar()
        if cpf in pedidos:
            del pedidos[cpf]
            self.salvar(pedidos)
            print(Cor.VERDE + "✅ Pedido de adoção removido com sucesso." + Cor.RESET)
        else:
            print(Cor.VERMELHO + "❌ Pedido de adoção não encontrado." + Cor.RESET)
