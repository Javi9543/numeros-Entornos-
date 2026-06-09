import pytest

from app.main import sumarNumeros

def testSumaPositivos():
    resultado = sumarNumeros(2,2)
    assert resultado == 4

def testSumaNegativos():
    resultado = sumarNumeros(-4, -5)
    assert resultado == -9
