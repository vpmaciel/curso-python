if __name__ == "__main__":
    idade = int(input("Digite a idade da pessoa: "))
    if 0 <= idade <= 12:
        print("Crianca.")
    elif 13 <= idade <= 17:
        print("Adolescente.")
    elif 18 <= idade <= 59:
        print("Adulto.")
    elif idade > 59:
        print("Idoso")
    else:
        print("Digíto uma idade válida!")
    exit()