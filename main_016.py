def compara():
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite um número: "))

    if (n1 > n2):
        print(f"{n1} é maior que {n2}")
    elif(n1 < n2):
        print(f"{n1} é menor que {n2}")
    else:
        print(f"{n1} é igual a {n2}")   

if __name__ == "__main__":
    compara()
    exit()