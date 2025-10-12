def maior_idade():
    idade = int(input("Digite a sua idade: "))
    
    if(idade >= 18):
        print("Você é elegível para votar.")
    else:
        print("Você não é elegível para votar.")

if __name__ == "__main__":
    maior_idade()
    exit()