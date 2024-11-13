import json
import os
from time import sleep

adocaoData = os.path.join(os.path.dirname(__file__), 'adocaoData.json')
if not os.path.exists(adocaoData):
    with open(adocaoData, 'w') as adocaoDataArquivo:
        json.dump({}, adocaoDataArquivo)

def adicionarPedido(cpf, nome, idade, animalType, raca, genero):
    pedidos = []
    pedidos.append({cpf:{'nome':nome, 'idade': idade, 'animal': animalType, 'raça': raca, 'genero': genero}})    
    with open(adocaoData, 'w') as adocaoDataArquivo:
        json.dump(pedidos, adocaoDataArquivo, indent=4,ensure_ascii=False)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")

def excluirPedido(cpf):
    pedidos = []
    for pedido in pedidos:
        if pedido[cpf] == cpf:
            pedidos.remove(pedido)
    with open(adocaoData, 'w') as adocaoDataArquivo:
        json.dump(pedidos, adocaoDataArquivo, indent=4,ensure_ascii=False)
    print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")





def Adicionar_animal():
    print("Vamos cadastrar seu Pet! Ele pode fazer outra família muito feliz, nos ajude a encontrar o macth perfeito para seu bichinho!")
    nome = input("Como devemos chamar seu pet? ")
    especie = input("Qual é a espécie do seu pet? (Exemplo: Cachorro, Gato, etc.) ")
    genero = input("Qual é o gênero do seu pet? (Exemplo: Masculino, Feminino) ")
    raca = input("Qual é a raça do seu pet? (Exemplo: Labrador, Siames, SRD) ")
    idade = input("Qual é a idade do seu pet? (em anos)")
    personalidade = input("Como você descreveria a personalidade do seu pet?")

    print("Agora algumas informações médicas.")
    castracao = input("Seu pet é castrado? (Sim/Não) ")
    vacinas = input("As vacinas estão em dia? (Sim/Não) ")
    info_relevante = input("Há alguma informação relevante sobre seu pet que gostaria de compartilhar? (Exemplo: restrições alimentares, preferência por ambientes calmos, etc.) ")
    
    cadastro = {
        "Nome: " : nome,
        "Especie: ": especie,
        "Sexo ": genero,
        "Raca: ": raca,
        "Idade: ": idade,
        "Personalidade: ": personalidade,
        "Castrado? ": castracao.upper(),
        "Corretamente Vacinado? ": vacinas.upper(),
        "Alguma informacao relevante? ": info_relevante
    }
    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open("data.json", "r") as getdata:
            data = json.load(getdata)
    else:
        data = {}    
    data[len(data)] = cadastro     
    with open("data.json", "w") as save:
        json.dump(data, save, indent=4)
    print(f"Animal Cadastrado! O token do seu processo é: {len(data) - 1}")

def ListarAnimais(): 
    with open("data.json", "r") as view:
        data = json.load(view)
    for i, m in data.items():

        caracteristicas = [f"Animal número: {i}"]
        for x, n in m.items():
            caracteristicas.append(f"{x} {n}")
        
        print("\n".join(caracteristicas))
        print("\r") 






def menu_inicial():
    print("ADOTE PET")
    print("1 - MÓDULO DO USUÁRIOS ")
    print("2 - MÓDULO DO ANIMAL")
    print("3 - ADOTE UM PET")
    print("4 - SAIR ")

def menu_user():
    print("\nMENU USUÁRIOS:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. LISTAR UM USUÁRIO")
    print("6. VOLTAR AO MENU ANTERIOR")

def menu_adotar():
    print("\nMENU PEDIDOS DE ADOÇÃO:")
    print("1. CRIAR PEDIDO DE ADOÇÃO")
    print("2. LISTAR PEDIDOS DE ADOÇÃO")
    print("3. ATUALIZAR PEDIDO DE ADOÇÃO")
    print("4. EXCLUIR PEDIDO DE ADOÇÃO")
    print("5. LISTAR UM PEDIDO DE ADOÇÃO")
    print("6. VOLTAR AO MENU ANTERIOR")

def menu_animais():
    print("\nMENU ANIMAIS PARA ADOÇÃO:")
    print("1. ADICIONAR ANIMAL")
    print("2. LISTAR ANIMAIS")
    print("3. ATUALIZAR ANIMAL")
    print("4. EXCLUIR ANIMAL")
    print("5. LISTAR UM ANIMAL")
    print("6. VOLTAR AO MENU ANTERIOR")

def main(): 
    while True:
        menu_inicial()
        opcao_inicial = int(input("Escolha uma opção:\n>>>"))
        match opcao_inicial:
            case(1):
                print("Op 1")
            case(2):
                while True:
                    menu_animais()
                    escolha= input("Digite sua escolha! --> ")      
                    match escolha:
                        case "1":
                            Adicionar_animal()
                        case "2":
                            ListarAnimais()
                        case "6":
                            print("VOLTAR AO MENU ANTERIOR...")
                            sleep(3)
                            break 
            case(3):
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
                    elif(op ==4):
                        print("Insira o CPF relacionado ao pedido de adoção.")
                        cpf = input(">>>")
                        excluirPedido(cpf)
                    elif(op == 6):
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
            case(4):
                break

if __name__ == "__main__":
    main()