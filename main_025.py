if __name__ == "__main__":
    v1 = int(input("Digite um número: "))
    v2 = int(input("Digite um número: "))
    v3 = int(input("Digite um número: "))
    
    positivos = 0

    if(v1 > 0):
        positivos += 1
    if(v2 > 0):
        positivos += 1
    if(v3 > 0):
        positivos += 1
    
    if(positivos >= 2):
        print("Pelo menos dois números são positivos!")
    else:
        print("Menos de dois números são positivos!")        
    exit()