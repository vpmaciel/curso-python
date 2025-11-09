if __name__ == "__main__":
    valor_compra = float(input("Digite o valor da compra: "))
    valor_final = valor_compra
    if valor_compra > 100:
        valor_final = 0.9 * valor_compra   

    print(f"Valor final: {valor_final}")

    exit()