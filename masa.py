def kilogram_a_gram(kilogram):
    return kilogram * 1000

def kilogram_a_ton(kilogram):
    return kilogram / 1000

def gram_a_kilogram(gram):
    return gram / 1000

def gram_a_ton(gram):
    return gram / 1000000

def ton_a_kilogram(ton):
    return ton * 1000

def ton_a_gram(ton):
    return ton * 1000000

if __name__ == "__main__":
    # Ejemplo de uso de kilogramo a gramos
    kilogram = 2.5
    gram = kilogram_a_gram(kilogram)
    print(f"{kilogram} kilogramos son equivalentes a {gram} gramos.")
    # Ejemplo de uso de kilogramo a tonelada
    kilogram = 2.5
    ton = kilogram_a_ton(kilogram)
    print(f"{kilogram} kilogramos son equivalentes a {ton} toneladas.")
    # Ejemplo de uso de gramos a kilogramos
    gramos = 2.5
    kilogramos = gram_a_kilogram(gramos)
    print(f"{gramos} gramos son equivalentes a {kilogramos} kilogramos.")
