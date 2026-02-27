if __name__ == "__main__":
    
    print("Números múltiplos de 3, de 1 a 100: ", end='');

    for i in range(1, 101):
        if i % 3 == 0: print(f"{i} ", end='')    

    exit()