# personas.py
from datetime import date, datetime

# Lista "base de datos" simple en memoria
PERSONAS = []  # cada elemento será un dict con los datos validados

def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).
    Fórmula: IMC = peso (kg) / (altura (m))^2
    Valida valores razonables para evitar cálculos inválidos.
    """
    if not isinstance(peso_kg, (int, float)) or not isinstance(altura_m, (int, float)):
        raise TypeError("El peso y la altura deben ser numéricos (int o float).")
    if peso_kg <= 0 or peso_kg > 400:
        raise ValueError("Peso fuera de rango razonable (0 < peso <= 400).")
    if altura_m <= 0 or altura_m > 2.7:
        raise ValueError("Altura fuera de rango razonable (0 < altura <= 2.7 m).")
    return round(peso_kg / (altura_m ** 2), 2)

def validar_fecha_nacimiento(fecha_str: str) -> date:
    """
    Valida la fecha de nacimiento en formato YYYY-MM-DD.
    Reglas:
    - Debe tener formato válido.
    - No puede ser futura ni igual a hoy.
    - Edad resultante debe estar en rango (0 < edad <= 120).
    Devuelve date si es válida; si no, lanza excepción.
    """
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD (ej: 2008-03-15).")

    hoy = date.today()
    if fecha >= hoy:
        raise ValueError("La fecha de nacimiento no puede ser futura ni igual a hoy.")

    # Cálculo de la edad
    edad = hoy.year - fecha.year - ((hoy.month, hoy.day) < (fecha.month, fecha.day))
    if edad <= 0 or edad > 120:
        raise ValueError("Edad fuera de rango razonable (0 < edad <= 120).")

    return fecha

def calcular_edad(fecha_nac: date, ref: date | None = None) -> int:
    """
    Calcula la edad en años COMPLETA respecto a 'ref' 
    """
    if ref is None:
        ref = date.today()
   
    return ref.year - fecha_nac.year

def crear_persona(nombre: str, apellido: str, fecha_nac_str: str, peso_kg: float, altura_m: float) -> dict:
    """
    Crea y valida una persona:
    - Valida nombre y apellido (no vacíos).
    - Valida fecha de nacimiento.
    - Calcula IMC.
    - Calcula edad.
    - Guarda en PERSONAS y retorna el dict creado.
    """
    if not isinstance(nombre, str) or not isinstance(apellido, str):
        raise TypeError("Nombre y apellido deben ser cadenas de texto.")
    if not nombre.strip() or not apellido.strip():
        raise ValueError("Nombre y apellido no pueden estar vacíos.")

    fecha_nac = validar_fecha_nacimiento(fecha_nac_str)
    imc = calcular_imc(peso_kg, altura_m)
    edad = calcular_edad(fecha_nac) 

    persona = {
        "nombre": nombre.strip(),
        "apellido": apellido.strip(),
        "fecha_nacimiento": fecha_nac,
        "peso_kg": float(peso_kg),
        "altura_m": float(altura_m),
        "imc": imc,
        "edad": edad, 
    }

    PERSONAS.append(persona)
    return persona

def limpiar_personas():
    """Utilidad para tests: vacía la 'base de datos' en memoria."""
    PERSONAS.clear()
