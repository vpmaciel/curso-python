def verifica_se_par():
    n = int(input("Digite um número inteiro: "))
    
    mensagem = f"{n} é par" if n % 2 == 0 else f"{n} é impar"
    print(mensagem)

if __name__ == "__main__":
    verifica_se_par()
    exit()