if __name__ == "__main__":

    soma = 0

    for i in range(1, 101):                
        if i % 2 == 0:
            soma +=  i

    print("soma dos números pares de 1 a 100: ", soma)    

    soma = 0

    for i in range(1, 101):                
        if i % 2 != 0:
            soma +=  i            

    print("soma dos números ímpares de 1 a 100:", soma)    
    exit()