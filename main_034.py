if __name__ == "__main__":
    idade = int(input("Digite a idade: "))
    
    if idade > 60:
        print(f"Você é idoso.")   
    elif idade > 18:
        print(f"Você é maior de idade.")   
    else:
        print(f"Você é menor de idade.")   

    exit()