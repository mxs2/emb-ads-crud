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
        
        print("  -  ".join(caracteristicas))
        print("\r") 
        
"""def DeletarAdocao():
    with open("data.json", "r") as view:
        data = json.load(view)
    print("")"""
    

def _main_():
    check = True
    while check:
        print("Opções: \n --> 1 CRIAR \n --> 2 VIZUALIZAR")
        escolha= input("Digite sua escolha! --> ")
        
        match escolha:
            case "1":
                Adicionar_animal()
            case "2":
                ListarAnimais()
            case __:
                check = False
                
_main_()

    
