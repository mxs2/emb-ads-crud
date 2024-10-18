# Projeto ADS-B

## Desafio Escolhido
WIP (Work in Progress).

## Como Fazer um Pull Request

### Guia para Fazer um Pull Request da Branch `develop` via CLI

#### Introdução

Este guia orienta sobre como fazer um Pull Request (PR) a partir da branch `develop`, utilizando o rebase e algumas boas práticas. Além disso, mostraremos como fazer isso diretamente pela linha de comando.

### Passo a Passo

#### 1. Certifique-se de que está atualizado

Antes de iniciar, garanta que a branch `develop` esteja atualizada com o repositório remoto:

```bash
git checkout develop
git pull origin develop
```

#### 2. Crie uma nova branch

Crie uma nova branch a partir de `develop` para implementar suas alterações. Nomeie a branch de forma descritiva:

```bash
git checkout -b minha-feature
```

#### 3. Faça suas alterações

Implemente suas alterações no código e teste-as localmente. Quando estiver satisfeito, adicione e faça commit das suas mudanças:

```bash
git add .
git commit -m "Descrição das mudanças realizadas"
```

#### 4. Rebase sua branch

Antes de abrir o Pull Request, rebata sua branch com a `develop` para garantir que você esteja trabalhando com a versão mais recente:

```bash
git fetch origin
git rebase origin/develop
```

Se houver conflitos durante o rebase, resolva-os e continue:

```bash
git add <arquivo_resolvido>
git rebase --continue
```

#### 5. Push da branch

Após o rebase, envie suas alterações para o repositório remoto:

```bash
git push origin minha-feature --force
```

**Nota:** O uso de `--force` é necessário porque o rebase altera o histórico de commits.

#### 6. Abra o Pull Request via CLI

Você pode abrir o Pull Request diretamente da linha de comando usando a GitHub CLI. Certifique-se de que a GitHub CLI está instalada e configurada. Para instalar a GitHub CLI, siga as instruções [aqui](https://cli.github.com/). Utilize o seguinte comando:

```bash
gh pr create --base develop --head minha-feature --title "Título do PR" --body "Descrição detalhada do que foi feito."
```

#### 7. Boas Práticas

- **Descreva o PR claramente:** Inclua uma descrição detalhada das mudanças e o propósito do PR.
- **Revise seu código:** Sempre revise o código antes de enviar o PR.
- **Mantenha commits pequenos e significativos:** Foque em uma única tarefa ou funcionalidade por commit.
- **Comunique-se:** Informe sua equipe sobre suas alterações, especialmente se impactarem seu trabalho.
- **Teste:** Execute testes para garantir que suas alterações não introduzam novos bugs.

## Colaboradores

- [Mateus Xavier](mailto:mxs2@cesar.school)

Sinta-se à vontade para entrar em contato para sugestões ou colaborações!