class TiposDeVariaveis:
    variavelGlobal = 10

    def mostrar(self):
        variavelLocal = 5
        print(f"variavelGlobal: {self.variavelGlobal}")
        print(f"variavelLocal: {variavelLocal}")

if __name__ == "__main__":
    variaveis = TiposDeVariaveis()
    variaveis.mostrar()
    exit()