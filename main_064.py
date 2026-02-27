if __name__ == "__main__":

    def menu():

        while True:
            print("")
            print("Menu de opções:")
            print("1. Somar dois números")
            print("2. Subtrarir dois números")
            print("3. Multiplicar dois números")
            print("4. Dividir dois números")
            print("5. Sair")
            opcao = int(input("Escolha o número da opção: "))

            if opcao >= 1 and opcao <= 4:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))

            if opcao == 1:
                print(f"Resultado: {n1} + {n2} = {n1 + n2}")

            if opcao == 2:
                print(f"Resultado: {n1} - {n2} = {n1 - n2}")                

            if opcao == 3:
                print(f"Resultado: {n1} * {n2} = {n1 * n2}")

            if opcao == 4:
                if n2 == 0:
                    print("Divisor igual a zero.")
                else:
                    print(f"Resultado: {n1} / {n2} = {n1 / n2}")        

            if opcao == 5:
                print("Programa encerrado.")
                break
            
            if opcao < 1 or opcao > 5:                
                print("Opção inválida!")
    menu()
    exit()