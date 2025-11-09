if __name__ == "__main__":
    idade_pessoa1 = float(input("Digite a idade da primeira pessoa: "))
    idade_pessoa2 = float(input("Digite a idade da segunda pessoa: "))

    if idade_pessoa1 > idade_pessoa2:
        print(f"A primeira pessoa é mais velha.")   
    elif idade_pessoa1 < idade_pessoa2:
        print(f"A segunda pessoa é mais velha.")   
    else:
        print(f"As duas pessoas tem a mesma idade")

    exit()