import json
import os

def menu_inicial():
    print("ADOTE PET")
    print("1 - MÓDULO DO USUÁRIOS ")
    print("2 - ADOTE UM PET")
    print("3 - MÓDULO DO ANIMAL")
    print("4 - SAIR ")

def main(): 
    while True:
        menu_inicial()
        opcao_inicial = int(input("Escolha uma opção:\n>>>"))
        match opcao_inicial:
            case(1):
                print("Op 1")

if __name__ == "__main__":
    main()