def exibir():
    num1 = int(input('Digite um número inteiro: '))
    num2 = int(input('Digite um número inteiro: '))
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Erro: divisão por zero"
    modulo = num1 % num2 if num2 != 0 else "Erro: divisão por zero"
    # Exibe os resultados
    print("Soma:", soma)
    print("Subtração:", subtracao)
    print("Multiplicação:", multiplicacao)
    print("Divisão:", divisao)
    print("Módulo:", modulo)

if __name__ == "__main__":
    exibir()
    exit()