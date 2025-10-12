def mensagem():    
    primeiro_nome = input("Digite seu primeiro nome: ")    
    sobrenome = input("Digite seu sobrenome: ")
    mensagem = f"Bem vindo, {primeiro_nome} {sobrenome}"
    print(mensagem)

if __name__ == "__main__":
    mensagem()