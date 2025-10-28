import os
from collections import Counter

# Recebendo os dados do usuário
entrada = input("Digite um conjunto de números inteiros separados por vírgula: ")
# Convertendo a entrada em uma lista de inteiros
dados = [int(x.strip()) for x in entrada.split(",")]

# Calculando Média Aritmética Simples
media = sum(dados) / len(dados)

# Calculando Mediana
dados_ordenados = sorted(dados)
n = len(dados_ordenados)

if n % 2 == 1:
    # quantidade ímpar de elementos
    mediana = dados_ordenados[n // 2]
else:
    # quantidade par de elementos
    mediana = (dados_ordenados[n // 2 - 1] + dados_ordenados[n // 2]) / 2

# Calculando Moda
contagem = Counter(dados)
max_freq = max(contagem.values())
moda = [k for k, v in contagem.items() if v == max_freq]
moda_str = ', '.join(str(m) for m in moda)

# Exibindo resultados
print(f"Média Aritmética: {media}")
print(f"Mediana: {mediana}")
if len(moda) == len(dados):
    print("Moda: Não existe (todos os valores aparecem apenas uma vez)")
else:
    print(f"Moda: {moda_str}")

os.system("pause")
