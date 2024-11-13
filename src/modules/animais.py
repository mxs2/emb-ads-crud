import json
import os


class Animais:
    def __init__(self):
        self.animalData = os.path.join(
            os.path.dirname(__file__), "./db/animalData.json"
        )
        if not os.path.exists(self.animalData):
            with open(self.animalData, "w") as animalDataArquivo:
                json.dump({}, animalDataArquivo, indent=4)

    def carregar(self):
        with open(self.animalData, "r") as view:
            return json.load(view)

    def adicionar(self, nome, especie, genero, raca, idade):
        data = self.carregar()
        data[str(len(data))] = {
            "Nome": nome,
            "Especie": especie,
            "Genero": genero,
            "Raca": raca,
            "Idade": idade,
        }
        with open(self.animalData, "w") as save:
            json.dump(data, save, indent=4)
        print("Animal cadastrado com sucesso!")

    def listar(self):
        data = self.carregar()
        for i, m in data.items():
            print(f"Animal número {i}: {m}")

    def buscar(self, nome):
        data = self.carregar()
        for i, m in data.items():
            if m["Nome"] == nome:
                print(f"Animal número {i}: {m}")
                return
        print("Animal não encontrado.")

    def atualizar(self, nome, especie, genero, raca, idade):
        data = self.carregar()
        for i, m in data.items():
            if m["Nome"] == nome:
                m["Especie"] = especie
                m["Genero"] = genero
                m["Raca"] = raca
                m["Idade"] = idade
                with open(self.animalData, "w") as save:
                    json.dump(data, save, indent=4)
                print("Animal atualizado com sucesso.")
                return
        print("Animal não encontrado.")

    def remover(self, nome):
        data = self.carregar()
        for i, m in data.items():
            if m["Nome"] == nome:
                del data[i]
                with open(self.animalData, "w") as save:
                    json.dump(data, save, indent=4)
                print("Animal removido com sucesso.")
                return
        print("Animal não encontrado.")
