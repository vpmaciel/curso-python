if __name__ == "__main__":
    
    soma = 0

    for i in range(1, 6):
        numero = float(input(f"Digite o {i}° número:"));
        soma += numero

    media = soma / 5

    print(f"Média: {media}")    

    exit()