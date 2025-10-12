def maior_numero():
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite um número inteiro: "))
    n3 = int(input("Digite um número inteiro: "))

    maior = n1

    if(n2 > maior):
        maior = n2

    if(n3 > maior):
        maior = n3

    print(f"Maior número: {maior}")

if __name__ == "__main__":
    maior_numero()
    exit()