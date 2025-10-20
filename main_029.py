if __name__ == "__main__":
    valor_pre_pos = 10
    print(f"Valor inicial: {valor_pre_pos}")
    # Pré-incremento
    pre_incremento = valor_pre_pos + 1
    print(f"Ao aplicar pré-incremento (++valor): {pre_incremento}")
    # Pós-incremento
    pos_incremento = valor_pre_pos
    valor_pre_pos += 1
    print(f"Ao aplicar pós-incremento (valor++): {pos_incremento}")
    print(f"Valor final após pós-incremento: {valor_pre_pos}")
    exit()