# Jogo da Tabuada em Python

## Descrição

Este programa gera aleatoriamente operações de multiplicação entre **0 × 0** e **10 × 10**. O usuário deve informar a resposta da multiplicação. O programa verifica se a resposta está correta e exibe uma mensagem informando o resultado.

Após cada rodada, o usuário pode escolher continuar respondendo novas multiplicações ou encerrar a execução.

---

## Funcionalidades

- Geração aleatória de multiplicações.
- Verificação automática da resposta.
- Exibição de mensagem de acerto ou erro.
- Exibição do resultado correto em caso de erro.
- Opção para continuar jogando.
- Limpeza da tela entre as rodadas.
- Encerramento controlado pelo usuário.

---

## Código-Fonte

```python
import random
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    # Gera dois números aleatórios entre 0 e 10
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)

    resultado_correto = n1 * n2

    try:
        resposta = int(input(f"Quanto é {n1} x {n2}? "))
    except ValueError:
        print("Resposta inválida! Digite apenas números inteiros.")
    else:
        if resposta == resultado_correto:
            print("✅ Você acertou!")
        else:
            print("❌ Você errou!")
            print(f"O resultado correto é: {resultado_correto}")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

    if continuar != "s":
        print("Programa encerrado.")
        break

    limpar_tela()
```

---

## Explicação do Código

### Importação de Bibliotecas

```python
import random
import os
```

- `random`: utilizada para gerar números aleatórios.
- `os`: utilizada para executar comandos do sistema operacional.

### Função para Limpar a Tela

```python
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
```

Esta função identifica o sistema operacional:

- Windows → utiliza `cls`
- Linux/macOS → utiliza `clear`

---

### Estrutura Principal

```python
while True:
```

O laço `while True` mantém o programa em execução até que o usuário decida sair.

---

### Geração dos Números Aleatórios

```python
n1 = random.randint(0, 10)
n2 = random.randint(0, 10)
```

Gera dois números inteiros aleatórios entre 0 e 10.

---

### Cálculo da Resposta Correta

```python
resultado_correto = n1 * n2
```

Armazena o resultado correto da multiplicação.

---

### Entrada de Dados

```python
resposta = int(input(f"Quanto é {n1} x {n2}? "))
```

Solicita que o usuário informe a resposta.

---

### Tratamento de Erros

```python
try:
    ...
except ValueError:
```

Evita que o programa seja encerrado caso o usuário digite algo que não seja um número.

---

### Verificação da Resposta

```python
if resposta == resultado_correto:
```

Compara a resposta informada pelo usuário com o resultado correto.

---

### Continuação do Programa

```python
continuar = input("\nDeseja continuar? (s/n): ").strip().lower()
```

Recebe a escolha do usuário e converte para letras minúsculas.

---

### Encerramento

```python
if continuar != "s":
    break
```

Se o usuário digitar algo diferente de `s`, o programa será encerrado.

---

## Exemplo de Execução

```text
Quanto é 4 x 7? 28
✅ Você acertou!

Deseja continuar? (s/n): s
```

```text
Quanto é 8 x 9? 70
❌ Você errou!
O resultado correto é: 72

Deseja continuar? (s/n): n
Programa encerrado.
```

---

## Conceitos Trabalhados

- Variáveis
- Entrada e saída de dados
- Estruturas condicionais (`if/else`)
- Laços de repetição (`while`)
- Funções
- Bibliotecas (`random` e `os`)
- Tratamento de exceções (`try/except`)
- Operadores aritméticos
- Comparação de valores

---

## Nível de Dificuldade

**Iniciante**

Este projeto é ideal para praticar os primeiros conceitos da linguagem Python, especialmente estruturas de repetição, condicionais e manipulação de entradas do usuário.
