import json
import os

class Adocoes:
    def __init__(self):
        self.adocaoData = os.path.join(os.path.dirname(__file__), './db/adocaoData.json')
        if not os.path.exists(self.adocaoData):
            with open(self.adocaoData, 'w') as adocaoDataArquivo:
                json.dump({}, adocaoDataArquivo, indent=4)

    def carregar(self):
        with open(self.adocaoData, 'r') as view:
            return json.load(view)

    def adicionar(self, cpf, nome, idade, animalType, raca, genero):
        pedidos = self.carregar()
        pedidos[cpf] = {
            'nome': nome,
            'idade': idade,
            'animal': animalType,
            'raça': raca,
            'genero': genero
        }
        with open(self.adocaoData, 'w') as adocaoDataArquivo:
            json.dump(pedidos, adocaoDataArquivo, indent=4, ensure_ascii=False)
        print("Pedido de adoção adicionado com sucesso!")

    def listar(self):
        pedidos = self.carregar()
        for cpf, pedido in pedidos.items():
            print(f"CPF: {cpf}, Pedido: {pedido}")

    def buscar(self, cpf):
        pedidos = self.carregar()
        if cpf in pedidos:
            print(f"Pedido de adoção: {pedidos[cpf]}")
        else:
            print("Pedido de adoção não encontrado.")
    
    def remover(self, cpf):
        pedidos = self.carregar()
        if cpf in pedidos:
            del pedidos[cpf]
            with open(self.adocaoData, 'w') as adocaoDataArquivo:
                json.dump(pedidos, adocaoDataArquivo, indent=4)
            print("Pedido de adoção removido com sucesso.")
        else:
            print("Pedido de adoção não encontrado.")
