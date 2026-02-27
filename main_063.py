if __name__ == "__main__":
    
    senha_digitada = ""
    senha_correta = "1234"
    while senha_correta != senha_digitada:
        senha_digitada = input("Digite a senha:");
        if senha_digitada != senha_correta:
            print("Senha incorreta!")

    print("Senha correta ! ")
    exit()