if __name__ == "__main__":
    
    numero = int(input("Digite um número para calcular seu fatorial:"));

    fatorial = 1

    for i in range(1, numero + 1):
        fatorial = fatorial * i

    print(f"Fatorial: {fatorial}")
    exit()