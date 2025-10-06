import pytest
from datetime import date
import personas

def test_calcular_imc_correcto():
    assert personas.calcular_imc(70, 1.75) == 22.86
    assert personas.calcular_imc(60, 1.60) == 23.44

def test_calcular_imc_valores_invalidos():
    with pytest.raises(ValueError):
        personas.calcular_imc(-70, 1.75)
    with pytest.raises(ValueError):
        personas.calcular_imc(70, 0)
    with pytest.raises(TypeError):
        personas.calcular_imc("70", 1.75)

def test_validar_fecha_correcta():
    f = personas.validar_fecha_nacimiento("2000-05-15")
    assert isinstance(f, date)

def test_validar_fecha_futura():
    fecha_futura = str(date.today().replace(year=date.today().year + 1))
    with pytest.raises(ValueError):
        personas.validar_fecha_nacimiento(fecha_futura)

def test_validar_fecha_mal_formato():
    with pytest.raises(ValueError):
        personas.validar_fecha_nacimiento("15-05-2000")


def test_calcular_edad_correcta():
    fecha_nac = date(2000, 10, 1)
    ref = date(2024, 10, 1)
    edad = personas.calcular_edad(fecha_nac, ref)
    assert edad == 24  
def test_calcular_edad_detectar_bug():
    fecha_nac = date(2000, 12, 1)
    ref = date(2024, 10, 1)
    edad = personas.calcular_edad(fecha_nac, ref)
    assert edad != 23

def test_crear_persona_correcta():
    personas.limpiar_personas()
    p = personas.crear_persona("Juan", "Perez", "2000-05-15", 70, 1.75)
    assert p["nombre"] == "Juan"
    assert p["imc"] == 22.86
    assert "edad" in p
    assert len(personas.PERSONAS) == 1

def test_crear_persona_nombre_vacio():
    with pytest.raises(ValueError):
        personas.crear_persona("", "Perez", "2000-05-15", 70, 1.75)