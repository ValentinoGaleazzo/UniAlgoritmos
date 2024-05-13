def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    previo_valor = 0

    for letra in romano[::-1]:
        valor = valores[letra]
        if valor < previo_valor:
            decimal -= valor
        else:
            decimal += valor
        previo_valor = valor

    return decimal