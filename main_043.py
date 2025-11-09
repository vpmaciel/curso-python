if __name__ == "__main__":
    numero1 = float(input("Digite o valor do primeiro número: "))
    numero2 = float(input("Digite o valor do segundo número: "))
    operacao = input("Digite a operação (/,*,-,+): ")

    if operacao == "+":
        print(f"Valor final: {numero1} + {numero2} = {numero1 + numero2}")
    elif operacao == "/":
        if(numero2 != 0):
            print(f"Valor final: {numero1} / {numero2} = {numero1 / numero2}")
        else:
            print("O valor do número segundo número é igual a zero, não existe divisão por zero.")
    elif operacao == "-":
        print(f"Valor final: {numero1} - {numero2} = {numero1 - numero2}")
    elif operacao == "*":
        print(f"Valor final: {numero1} * {numero2} = {numero1 * numero2}")
    else:
        print("Digíto para operação inválido!")
    exit()