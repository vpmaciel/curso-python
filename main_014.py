def converte_farenheit():
    celsius = float(input("Digire a temperatura em graus celcius: "))    
    farenheit = (celsius * 9/5) + 32
    
    print(f"Temperatura em Farenheit é : {farenheit}")

if __name__ == "__main__":
    converte_farenheit()
    exit()