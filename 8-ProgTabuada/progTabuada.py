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

os.system("pause")