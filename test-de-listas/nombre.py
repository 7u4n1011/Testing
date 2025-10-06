def normalizar_nombres(nombres):
    """
    Recibe una lista de nombres (con posibles mayúsculas desordenadas o espacios)
    y devuelve una nueva lista con:
    - Espacios recortados (al inicio y al final)
    - Todas las palabras con la primera letra en mayúscula (title case)
    
    Si el parámetro no es una lista, lanza un TypeError.
    """
    # Validamos que sea una lista
    if type(nombres) != list:
      raise TypeError("Se esperaba una lista de nombres.")

    # Creamos una lista vacía para guardar los nombres normalizados
    nombres_normalizados = []

    # Recorremos cada nombre de la lista original
    for nombre in nombres:
           nombre_str = str(nombre) # Convertimos el valor a string (por si viene como número u otro tipo)
           nombre_limpio = nombre_str.strip()  # Quitamos espacios extra al inicio y al final
           nombre_titulo = nombre_limpio.title()# Convertimos a formato título (primera letra de cada palabra en mayúscula)
           nombres_normalizados.append(nombre_titulo)# Agregamos el resultado a la nueva lista

    # Devolvemos la lista nueva
    return nombres_normalizados


def indice_de(nombres, nombre_busqueda):
    """
    Devuelve el índice de 'nombre_busqueda' en la lista 'nombres'.
    Si no está, retorna -1.
    Supone que la lista ya está normalizada.
    """
    i = 0
    for nombre in nombres:
        if nombre == nombre_busqueda:
            return i
        i += 1
    return -1

def duplicados(nombres):
    resultado = []
    for nombre in nombres:
        if nombre in resultado:
            continue
        else:
            resultado.append(nombre)
    return resultado