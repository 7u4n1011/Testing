import pytest
from calculadora import sumar, restar, dividir

def test():
    assert sumar(2, 3) == 5
    assert restar(-1, 1) == -2