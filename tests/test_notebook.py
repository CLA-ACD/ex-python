import nbformat
from nbconvert import PythonExporter
import pytest

#Cargar el notebook
with open('notebook.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

    python_exporter = PythonExporter()
    python_code, _ = python_exporter.from_notebook_node(nb)

    # Ejecutar el código del notebook
    exec(python_code)

# Definir los tests
def test_area_triangulo():
    assert area_triangulo(3, 6) == 9
    assert area_triangulo(0, 0) == 0
    assert area_triangulo(2, 5) == 5
    assert area_triangulo(7, 4) == 14

def test_mayor_de_tres():
    assert mayor_de_tres(3, 6, 9) == 9
    assert mayor_de_tres(9, 6, 3) == 9
    assert mayor_de_tres(3, 9, 6) == 9
    assert mayor_de_tres(5, 5, 5) == 5

def test_cantidad_impares():
    assert cantidad_impares([1, 2, 3, 4, 5]) == 3
    assert cantidad_impares([2, 4, 6, 8, 10]) == 0
    assert cantidad_impares([1, 3, 5, 7, 9]) == 5
    assert cantidad_impares([]) == 0

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

def test_es_palindromo():
    assert es_palindromo("reconocer") == True
    assert es_palindromo("hola") == False
    assert es_palindromo("anitalavalatina") == True
    assert es_palindromo("radar") == True
    assert es_palindromo("python") == False




