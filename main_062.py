if __name__ == "__main__":
    
    numero = int(input("Digite um número inteiro menor que 1000:"));
    
    while numero <= 1000:
        numero *= 2;
        
    print("Número final: ", numero)
    exit()