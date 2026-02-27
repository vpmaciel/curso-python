if __name__ == "__main__":
    
    numero = int(input("Digite um número (número negativo para terminar):"));
    contagem = 0
    while numero >= 0:
        numero = int(input("Digite um número (número negativo para terminar):"));
        contagem += 1

    print("Total de números positivos: ", contagem)
    exit()