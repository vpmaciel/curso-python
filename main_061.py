if __name__ == "__main__":
    
    numero = int(input("Digite um número inteiro positivo: "));
    
    raiz = 0
    while ((raiz + 1) * (raiz + 1)) <= numero:        
        raiz += 1

    print("Raiz: ", raiz)
    exit()