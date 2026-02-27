if __name__ == "__main__":
    
    print(f"Sequência de fibonacci:")    

    anterior = 0
    proximo = 1
    f = 0

    for i in range(1, 11):        
        print(f"{f} ", end='')    
        f = anterior + proximo
        anterior = proximo
        proximo = f
    exit()