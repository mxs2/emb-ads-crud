import json
import os

adocaoData = os.path.join(os.path.dirname(__file__), 'adocaoData.json')
if not os.path.exists(adocaoData):
    with open(adocaoData, 'w') as adocaoDataArquivo:
        json.dump({}, adocaoDataArquivo)
        
#Escrever dados no json
"""with open(adocaoData, 'w') as adocaoDataArquivo:
        json.dump(dicionario, adocaoDataArquivo, indent=4)"""

def adicionarPedido(cpf, nome, idade, animalType, raca, genero):
    pedidos = []
    pedidos.append({cpf:{'nome':nome, 'idade': idade, 'animal': animalType, 'raça': raca, 'genero': genero}})    
    with open(adocaoData, 'w') as adocaoDataArquivo:
        json.dump(pedidos, adocaoDataArquivo, indent=4,ensure_ascii=False)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")

def menu_adotar():
    print("\nMENU PEDIDOS DE ADOÇÃO:")
    print("1. CRIAR PEDIDO DE ADOÇÃO")
    print("2. LISTAR PEDIDOS DE ADOÇÃO")
    print("3. ATUALIZAR PEDIDO DE ADOÇÃO")
    print("4. EXCLUIR PEDIDO DE ADOÇÃO")
    print("5. LISTAR UM PEDIDO DE ADOÇÃO")
    print("6. VOLTAR AO MENU ANTERIOR")

def main():
    while True:
        menu_adotar()
        op = int(input("O que você deseja?"))
        if(op == 1):
            cpf = input("Insira seu CPF: ")
            nome = input("Insira seu nome: ")
            idade = input("Insira sua idade: ")
            animalType = input("Qual animal você deseja? (Gato/Cachorro): ")
            raca = input("Qual a raça desejada: ")
            genero = input("Qual o gênero desejado: ")
            adicionarPedido(cpf, nome, idade, animalType, raca, genero)

if __name__ == "__main__":
    main()