def romano_a_decimal(romano, previo_valor=0):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if not romano:
        return 0
    
    letra = romano[-1]
    valor = valores[letra]
    
    if valor < previo_valor:
        return -valor + romano_a_decimal(romano[:-1], valor)
    else:
        return valor + romano_a_decimal(romano[:-1], valor)