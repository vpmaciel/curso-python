if __name__ == "__main__":
    
    numero = int(input("Digite um número (0 para terminar):"));
    soma = numero
    while numero != 0:
        numero = int(input("Digite um número (0 para terminar):"));
        soma += numero

    print("Soma: ", soma)
    exit()