import json
import os

adocaoData = os.path.join(os.path.dirname(__file__), 'adocaoData.json')
if not os.path.exists(adocaoData):
    with open(adocaoData, 'w') as adocaoDataArquivo:
        json.dump({}, adocaoDataArquivo)
#Escrever dados no json
"""with open(adocaoData, 'w') as adocaoDataArquivo:
        json.dump(dados, adocaoDataArquivo, indent=4)"""