import json
import os


class Cor:
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    RESET = "\033[0m"


class Animais:
    def __init__(self):
        self.animalData = os.path.join(
            os.path.dirname(__file__), "./db/animalData.json"
        )
        if not os.path.exists(self.animalData):
            with open(self.animalData, "w") as animalDataArquivo:
                json.dump({}, animalDataArquivo, indent=4)

    def carregar(self):
        try:
            with open(self.animalData, "r") as view:
                return json.load(view)
        except json.JSONDecodeError:
            print(
                Cor.VERMELHO
                + "Erro ao carregar dados: arquivo JSON inválido."
                + Cor.RESET
            )
            return {}

    def salvar(self, data):
        with open(self.animalData, "w") as save:
            json.dump(data, save, indent=4, ensure_ascii=False)

    def adicionar(self, nome, especie, genero, raca, idade):
        data = self.carregar()
        novo_id = str(len(data) + 1)
        data[novo_id] = {
            "Nome": nome,
            "Especie": especie,
            "Genero": genero,
            "Raca": raca,
            "Idade": idade,
        }
        self.salvar(data)
        print(Cor.VERDE + "✅ Animal cadastrado com sucesso!" + Cor.RESET)

    def listar(self):
        data = self.carregar()
        if data:
            print(Cor.AZUL + "Lista de Animais Cadastrados:" + Cor.RESET)
            for i, m in data.items():
                print(Cor.AZUL + f"\nAnimal ID {i}:" + Cor.RESET)
                for chave, valor in m.items():
                    print(f"  {chave}: {valor}")
            print(Cor.AZUL + "\nFim da Lista" + Cor.RESET)
        else:
            print(Cor.AMARELO + "⚠️ Nenhum animal cadastrado." + Cor.RESET)

    def buscar(self, nome):
        data = self.carregar()
        encontrado = False
        for i, m in data.items():
            if m["Nome"].lower() == nome.lower():
                print(Cor.VERDE + f"✅ Animal encontrado (ID {i}):" + Cor.RESET)
                for chave, valor in m.items():
                    print(f"  {chave}: {valor}")
                encontrado = True
                break
        if not encontrado:
            print(Cor.VERMELHO + "❌ Animal não encontrado." + Cor.RESET)

    def atualizar(self, nome, especie, genero, raca, idade):
        data = self.carregar()
        atualizado = False
        for i, m in data.items():
            if m["Nome"].lower() == nome.lower():
                m.update(
                    {"Especie": especie, "Genero": genero, "Raca": raca, "Idade": idade}
                )
                self.salvar(data)
                print(Cor.VERDE + "✅ Animal atualizado com sucesso." + Cor.RESET)
                atualizado = True
                break
        if not atualizado:
            print(Cor.VERMELHO + "❌ Animal não encontrado." + Cor.RESET)

    def remover(self, nome):
        data = self.carregar()
        removido = False
        for i, m in list(data.items()):
            if m["Nome"].lower() == nome.lower():
                del data[i]
                self.salvar(data)
                print(Cor.VERDE + "✅ Animal removido com sucesso." + Cor.RESET)
                removido = True
                break
        if not removido:
            print(Cor.VERMELHO + "❌ Animal não encontrado." + Cor.RESET)
