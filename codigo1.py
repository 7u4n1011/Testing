# Crea una funcion para calcular promedio
def calcular_promedio (numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma / len(numeros) # 'len' longitud de lista

# Crea una lista con elementos
lista = [10, 20, 30, 40]

# Imprime por pantalla el resultado
print (calcular_promedio(lista))