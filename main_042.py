if __name__ == "__main__":
    nota = int(input("Digite o valor da nota (0 até 10): "))
    
    if nota == 10:
        print(f"Excelente.")
    elif nota == 8 or nota == 9:
        print(f"Muito bom.")
    elif nota == 6 or nota == 7:
        print(f"Bom.")
    elif nota == 5:
        print(f"Regular.")    
    elif nota < 5 and nota >= 0:
        print(f"Insuficiente")    
    else:
        print("Nota inválida")

    exit()