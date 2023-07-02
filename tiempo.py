def segundo_a_minutos(segundo):
    return segundo / 60

def segundo_a_horas(segundo):
    return segundo / 3600

def minutos_a_segundo(minutos):
    return minutos * 60

def minutos_a_horas(minutos):
    return minutos / 60

def horas_a_segundo(horas):
    return horas * 3600

def horas_a_minutos(horas):
    return horas * 60

if __name__ == "__main__":
    # Ejemplo de uso de segundo a minuto
    segundo = 150
    minutos = segundo_a_minutos(segundo)
    print(f"{segundo} segundos son equivalentes a {minutos} minutos.")

    # Ejemplo de uso de segundo a horas
    segundo = 150
    horas = segundo_a_horas(segundo)
    print(f"{segundo} segundos son equivalentes a {horas} horas.")

    # Ejemplo de uso de minutos a segundo
    minutos = 150
    segundos = segundo_a_minutos(minutos)
    print(f"{minutos} segundos son equivalentes a {segundos} minutos.")

    #continua invocando para el resto
