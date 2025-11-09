if __name__ == "__main__":
    dia = int(input("Digite um número para o dia da semana (1 até 7): "))
    
    if dia == 1:
        print(f"{dia} é igual a domingo.")
    elif dia == 2:
        print(f"{dia} é igual a segunda.")
    elif dia == 3:
        print(f"{dia} é igual a terça.")
    elif dia == 4:
        print(f"{dia} é igual a quarta.")
    elif dia == 5:
        print(f"{dia} é igual a quinta.")
    elif dia == 6:
        print(f"{dia} é igual a sexta.")
    elif dia == 7:
        print(f"{dia} é igual a sábado.")
    else:
        print("Número inválido digite um número de 1 até 7")

    exit()