if __name__ == "__main__":
    n1 = float(input("Digite um número "))
    n2 = float(input("Digite um número "))
    n3 = float(input("Digite um número "))
    
    if n1 == n2 == n3:
        print(f"Todos os números são iguais.")   
    elif n1 > n2 > n3:
        print(f"{n1} é o maior.")   
    elif n2 > n1 > n3:
        print(f"{n2} é o maior.")
    else:
        print(f"{n3} é o maior")

    exit()