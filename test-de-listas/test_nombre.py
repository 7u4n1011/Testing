import pytest 
from nombre import indice_de, duplicados, normalizar_nombres as norm

def test_normalizar():
    entrada = ["juan", "maria", "sofia"]
    salida = ["Juan", "Maria", "Sofia"]
    assert norm(entrada) == salida

def test_indice_de():
    assert indice_de(["Ana", "Juan", "Maria"], "Juan") == 1
    assert indice_de(["Ana", "Juan", "Maria"], "Pedro") == -1
    assert indice_de([], "Cualquiernombre") == -1
    assert indice_de(["SoloUnNombre"], "SoloUnNombre") == 0
    assert indice_de(["Ana", "Juan", "Maria"], "") == -1

def test_duplicados():
    assert duplicados(["Ana", "Juan", "Maria", "Ana", "Juan"]) == ["Ana", "Juan", "Maria"]
    assert duplicados(["Martin", "Jose", "Mateo", "Jose", "Mateo"]) == ["Martin", "Jose", "Mateo"]
    assert duplicados([]) == []
    assert duplicados(["SoloUnNombre"]) == ["SoloUnNombre"]
    assert duplicados(["Maxi", "Maxi", "Maxi"]) == ["Maxi"]