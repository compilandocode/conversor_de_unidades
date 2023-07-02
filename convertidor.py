import temperatura
import masa
import tiempo

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Celsius" and unidad_destino == "Fahrenheit":
        return temperatura.celsius_a_fahrenheit(valor)
    elif unidad_origen == "Celsius" and unidad_destino == "Kelvin":
        return temperatura.celsius_a_kelvin(valor)
    elif unidad_origen == "Fahrenheit" and unidad_destino == "Celsius":
        return temperatura.fahrenheit_a_celsius(valor)
    elif unidad_origen == "Fahrenheit" and unidad_destino == "Kelvin":
        return temperatura.fahrenheit_a_kelvin(valor)
    elif unidad_origen == "Kelvin" and unidad_destino == "Celsius":
        return temperatura.kelvin_a_celsius(valor)
    elif unidad_origen == "Kelvin" and unidad_destino == "Fahrenheit":
        return temperatura.kelvin_a_fahrenheit(valor)
    else:
        return None

def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Kilogramo" and unidad_destino == "Gramo":
        return masa.kilogram_a_gram(valor)
    elif unidad_origen == "Kilogramo" and unidad_destino == "Tonelada":
        return masa.kilogram_a_ton(valor)
    elif unidad_origen == "Gramo" and unidad_destino == "Kilogramo":
        return masa.gram_a_kilogram(valor)
    elif unidad_origen == "Gramo" and unidad_destino == "Tonelada":
        return masa.gram_a_ton(valor)
    elif unidad_origen == "Tonelada" and unidad_destino == "Kilogramo":
        return masa.ton_a_kilogram(valor)
    elif unidad_origen == "Tonelada" and unidad_destino == "Gramo":
        return masa.ton_a_gram(valor)
    else:
        return None

def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Segundo" and unidad_destino == "Minuto":
        return tiempo.segundo_a_minutos(valor)
    elif unidad_origen == "Segundo" and unidad_destino == "Hora":
        return tiempo.segundo_a_horas(valor)
    elif unidad_origen == "Minuto" and unidad_destino == "Segundo":
        return tiempo.minutos_a_segundo(valor)
    elif unidad_origen == "Minuto" and unidad_destino == "Hora":
        return tiempo.minutos_a_horas(valor)
    elif unidad_origen == "Hora" and unidad_destino == "Segundo":
        return tiempo.horas_a_segundo(valor)
    elif unidad_origen == "Hora" and unidad_destino == "Minuto":
        return tiempo.horas_a_minutos(valor)
    else:
        return None

if __name__ == "__main__":
    # Ejemplo de uso para usar el modulo temperatura / de celsius a fahrenheit
    valor = 20
    unidad_origen = "Celsius"
    unidad_destino = "Fahrenheit"
    resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
    print(f"{valor} grados {unidad_origen} son equivalentes a {resultado} grados {unidad_destino}.")

    # Ejemplo de uso para usar el modulo masa / de kilogramo a gramo
    valor = 100
    unidad_origen = "Kilogramo"
    unidad_destino = "Gramo"
    resultado = convertir_masa(valor, unidad_origen, unidad_destino)
    print(f"{valor} de {unidad_origen} son equivalentes a {resultado}  {unidad_destino}s.")

    # Ejemplo de uso para usar el modulo tiempo / Segundo a minutos
    valor = 70
    unidad_origen = "Segundo"
    unidad_destino = "Minuto"
    resultado = convertir_tiempo(valor, unidad_origen, unidad_destino)
    print(f"{valor}  {unidad_origen} son equivalentes a {resultado:.2f}  {unidad_destino}s.")
