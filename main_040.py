if __name__ == "__main__":
    velocidade = float(input("Digite a velocidade em (km/h): "))
    
    if velocidade <= 60:
        print(f"Dentro do limite de velocidade.")   
    elif velocidade <= 80:
        print(f"Acima do limite")   
    else:
        print(f"Muito acima do limite.")

    exit()