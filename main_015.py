def potencia():
    
    base = int(input("Digite um número para ser a base: "))
    expoente = int(input("Digite um número para ser o expoente: "))
    resultado = pow(base, expoente)
    print(f"Resultado de {base} elevado a {expoente}: {resultado}")

if __name__ == "__main__":
    potencia()
    exit()