def constantes():
    PI = 3.15159    
    print(f"PI: {PI}")

    try:
        PI = 5
    except Exception as e:
        print(e)
        
    print(f"PI: {PI}")
    

if __name__ == "__main__":
    constantes()
    exit()