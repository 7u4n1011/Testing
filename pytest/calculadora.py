# calculadora.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    #raise Se usa cuando querés detener la ejecución del programa y avisar que algo no está bien
    return a / b
