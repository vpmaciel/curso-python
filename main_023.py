if __name__ == "__main__":
    idade1 = int(input("Digite a idade: "))
    idade2 = int(input("Digite a idade: "))
    idade3 = int(input("Digite a idade: "))
    maior_idade = 0

    if(idade1 >= 18):
        maior_idade += 1
    if(idade2 >= 18):
        maior_idade += 1     
    if(idade3 >= 18):
        maior_idade += 1     

    if(maior_idade >= 2):
        print("Pelo menos duas pessoas são maiores de idade!")
    else:
        print("Não temos mais de duas pessoas maiores de idade!")
    exit()