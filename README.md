# Ejercio - Autograding Jupyter Notebook

Resuelve los ejercicios indicados en el Jupyter Notebook `notebook.ipynb`

# Comandos

## Instalación de dependencias

Para consultar los programas y bibliotecas disponibles para el ejercicio puede usar los comandos:
```
pytest --version
pip list | grep nbformat
pip list | grep nbconvert
```

Si faltara alguna puede instalarla con el siguiente comando:

```
pip install pytest nbformat nbconvert
```

## Ejecución de todas las pruebas locales
```
pytest -p no:warnings tests/
```
## Ejecución de pruebas individuales
```
pytest -p no:warnings -k "test_area_triangulo" tests/
pytest -p no:warnings -k "test_mayor_de_tres" tests/
pytest -p no:warnings -k "test_cantidad_impares" tests/
pytest -p no:warnings -k "test_factorial" tests/
pytest -p no:warnings -k "test_es_palindromo" tests/
```

## Comandos Git-Cambios y envío a Autograding

### Por cada cambio importante que haga, actualice su historia usando los comandos:
```
git add .
git commit -m "Descripción del cambio"
```
### Envíe sus actualizaciones a GitHub para Autograding con el comando:
```
git push origin main
```
