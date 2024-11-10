import json
import os

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
        
"""def DeletarAdocao():
    with open("data.json", "r") as view:
        data = json.load(view)
    print("")"""



def menu_animais():
    print("\nMENU ANIMAIS PARA ADOÇÃO:")
    print("1. ADICIONAR ANIMAL")
    print("2. LISTAR ANIMAIS")
    print("3. ATUALIZAR ANIMAL") 
    print("4. EXCLUIR ANIMAL")
    print("5. LISTAR UM ANIMAL")
    print("6. VOLTAR AO MENU ANTERIOoR")
    
def _main_():
    while True:
        menu_animais();
        op_moduloAnimal = int(input("ESCOLHA UMA OPÇÃO:\n>>>"))
        if (op_moduloAnimal == 1):
            print("\n<<< ADICIONAR ANIMAL SELECIONADO >>>")
            Adicionar_animal();
        elif (op_moduloAnimal == 2):
            print("\n<<< LISTAR ANIMAIS SELECIONADO >>>")
            ListarAnimais();
        elif (op_moduloAnimal == 3):
            print("\n<<< ATUALIZAR ANIMAL SELECIONADO >>>")
        elif (op_moduloAnimal == 4):
            print("\n<<< EXCLUIR ANIMAL SELECIONADO >>>")
        elif (op_moduloAnimal == 5):
            print("\n<<< LISTAR UM ANIMAL SELECIONADO >>>")
        elif (op_moduloAnimal == 6):
            print("\n<<< VOLTAR AO MENU ANTERIOR SELECIONADO >>>")
        """elif (op_moduloAnimal ):
            print("\nOpção Invalida. Tente Novamente!")"""
  
_main_()