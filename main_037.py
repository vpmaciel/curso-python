if __name__ == "__main__":
    temperatura = float(input("Digite a temperatura: "))
    
    if temperatura > 30:
        print(f"Clima está quente.")   
    elif temperatura >= 15:
        print(f"Clima está agradável.")   
    else:
        print(f"Clima está frio")

    exit()