if __name__ == "__main__":
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))
    n3 = int(input("Digite um número: "))

    if(n1 > 10 or n2 > 10 or n3 > 10):
        print("Pelo menos um dos números é maior que 10!")
    else:
        print("Nenhum dos números é maior que 10!")
    
    if(n1 > 10 and n2 > 10 and n3 > 10):
        print("Os três números são maiores que 10!")
    else:
        print("Algun(s) do(s) números é(são) menor(es) que 10!")        

    exit()