import pytest
from login import validar_login as val

def test_validar():
    #assert val ("","") == "El nombre de usuario no puede estar vacío."
    assert val ("Juan","123abc") == "Acceso concedido"
    #assert val ("Juan","123ab") == "La contraseña debe tener al menos 6 caracteres."
    assert val ("Juan"," ") == "La contraseña no puede contener espacios."
