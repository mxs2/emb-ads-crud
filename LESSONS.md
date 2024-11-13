# Lições para Apresentação

Os sistemas permitem adicionar, listar, buscar, atualizar e remover pedidos de adoção. Utiliza-se a biblioteca `json` para manipular o arquivo de dados e `os` para garantir o caminho correto do arquivo.

## Uso do self 
O self se refere à instância atual de uma classe, permitindo acessar seus atributos e métodos. Ele é necessário para distinguir atributos de instância de variáveis locais.

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # Atributo de instância

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}")

# Criando instâncias
pessoa1 = Pessoa("Ale")
pessoa2 = Pessoa("Raphael")

# Chamando o método cumprimentar
pessoa1.cumprimentar()  
pessoa2.cumprimentar()  
```
Output:
```
Olá, meu nome é Ale
Olá, meu nome é Raphael
```



## Dependências

Para que o código funcione, certifique-se de que você tenha um diretório `db` com um arquivo `adocaoData.json` vazio ou que permita que o script crie esse arquivo. Abaixo, veja uma descrição das bibliotecas e classes envolvidas:

### Importações

```python
import json
import os
```

- `json`: Permite ler e escrever dados em formato JSON.
- `os`: Garante a manipulação correta do sistema de arquivos, como obter o caminho correto do arquivo de dados.

### Classe `Cor`

A classe `Cor` define algumas constantes para usar cores no terminal, melhorando a visualização das mensagens de sucesso, erro e avisos.

```python
class Cor:
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    RESET = "\033[0m"
```

### Classe `Adocoes`

A classe principal `Adocoes` possui vários métodos para gerenciar os pedidos de adoção. Veja como cada um funciona:

```python
class Adocoes:
    def __init__(self):
        self.adocaoData = os.path.join(
            os.path.dirname(__file__), "./db/adocaoData.json"
        )
        # Cria o arquivo vazio se ele não existir
        if not os.path.exists(self.adocaoData):
            with open(self.adocaoData, "w") as adocaoDataArquivo:
                json.dump({}, adocaoDataArquivo, indent=4)
```

- `__init__`: Inicializa a classe e cria o arquivo `adocaoData.json` se ele não existir.

### Métodos da Classe

#### 1. `carregar()`

Carrega os dados do arquivo JSON. Em caso de erro, retorna um dicionário vazio e exibe uma mensagem de erro.

```python
def carregar(self):
    try:
        with open(self.adocaoData, "r") as adocaoDataArquivo:
            return json.load(adocaoDataArquivo)
    except json.JSONDecodeError:
        print(Cor.VERMELHO + "Erro ao carregar dados: arquivo JSON inválido." + Cor.RESET)
        return {}
```

> O JSONDecodeError é uma exceção lançada em Python quando ocorre um erro ao tentar decodificar (ou carregar) um arquivo ou string no formato JSON.

#### 2. `salvar(pedidos)`

Salva os dados no arquivo JSON. Recebe um dicionário `pedidos` como parâmetro.

```python
def salvar(self, pedidos):
    with open(self.adocaoData, "w") as adocaoDataArquivo:
        json.dump(pedidos, adocaoDataArquivo, indent=4, ensure_ascii=False)
```

#### 3. `adicionar(cpf, nome, idade, animalType, raca, genero)`

Adiciona um novo pedido de adoção ao arquivo. Exemplo de uso:

```python
adocao.adicionar("12345678900", "Maria Silva", 30, "Cachorro", "Labrador", "Fêmea")
```

```python
def adicionar(self, cpf, nome, idade, animalType, raca, genero):
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
```

#### 4. `listar()`

Lista todos os pedidos de adoção. Exibe uma mensagem caso nenhum pedido seja encontrado.

```python
def listar(self):
    pedidos = self.carregar()
    if pedidos:
        print(Cor.AZUL + "Lista de Pedidos de Adoção:" + Cor.RESET)
        for cpf, pedido in pedidos.items():
            print(f"CPF: {cpf}, Pedido: {pedido}")
    else:
        print(Cor.AMARELO + "⚠️ Nenhum pedido de adoção encontrado." + Cor.RESET)
```

#### 5. `buscar(cpf)`

Busca um pedido específico pelo CPF. Exemplo de uso:

```python
adocao.buscar("12345678900")
```

```python
def buscar(self, cpf):
    pedidos = self.carregar()
    if cpf in pedidos:
        print(Cor.VERDE + "✅ Pedido de adoção encontrado:" + Cor.RESET)
        print(f"CPF: {cpf}, Pedido: {pedidos[cpf]}")
    else:
        print(Cor.VERMELHO + "❌ Pedido de adoção não encontrado." + Cor.RESET)
```

#### 6. `atualizar(cpf, nome, idade, animalType, raca, genero)`

Atualiza um pedido existente pelo CPF. Exemplo de uso:

```python
adocao.atualizar("12345678900", "Maria Silva", 31, "Gato", "Siamês", "Macho")
```

```python
def atualizar(self, cpf, nome, idade, animalType, raca, genero):
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
```

#### 7. `remover(cpf)`

Remove um pedido de adoção pelo CPF. Exemplo de uso:

```python
adocao.remover("12345678900")
```

```python
def remover(self, cpf):
    pedidos = self.carregar()
    if cpf in pedidos:
        del pedidos[cpf]
        self.salvar(pedidos)
        print(Cor.VERDE + "✅ Pedido de adoção removido com sucesso." + Cor.RESET)
    else:
        print(Cor.VERMELHO + "❌ Pedido de adoção não encontrado." + Cor.RESET)
```

## Exemplo Completo de Uso

```python
# Inicialização
adocao = Adocoes()

# Adicionar um pedido de adoção
adocao.adicionar("12345678900", "Maria Silva", 30, "Cachorro", "Labrador", "Fêmea")

# Listar todos os pedidos
adocao.listar()

# Buscar um pedido específico
adocao.buscar("12345678900")

# Atualizar um pedido de adoção
adocao.atualizar("12345678900", "Maria Silva", 31, "Gato", "Siamês", "Macho")

# Remover um pedido de adoção
adocao.remover("12345678900")
```