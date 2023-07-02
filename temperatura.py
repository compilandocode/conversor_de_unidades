def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def kelvin_a_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

if __name__ == "__main__":
    # Ejemplo de uso de celsius a fahrenheit 
    celsius = 25
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")

    # Ejemplo de uso de celsius a kelvin 
    celsius = 25
    fahrenheit = celsius_a_kelvin(celsius)
    print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Kelvin.")

    # Ejemplo de uso de fahrenheit a celsius
    fahrenheit = 250
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius:.2f} grados Celsius.")
    # Continua, solo es invocar a las funciones 