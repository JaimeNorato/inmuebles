# Proyecto Api Inmueble

Para el desarrollo de la prueba se tratará de usar las tecnologías menos invasivas que no ofrezcan en lo posible ningún tipo de ayuda a nivel estructural o práctica de programación, con el propósito de que se pueda demostrar las buenas prácticas

Se iniciará levantando el servidor web para la exposición de los endpoinds y luego se establecerá las conexiones con la BD

Después se empezará a generar una estructura eficienta para la consulta a la BD, ya que no se usara ningún ORM, estableciendo unos modelos que se encarguen de la consulta

durante el desarrollo se usará la estrategia gitFlow para el manejo de las ramas con git 

## Tecnologías
A continuación se detalla las tecnologías usadas en el desarrollo del api

### Flask
- Para levantar el servidor se usara Flask, para levantar el servidor web, se usara este en lugar de FastApi, ya que al ser un micro framework, no incluye muchas herramientas, lo que permite cumplir con el objetivo de la prueba para poder demostrar las buenas prácticas de programación


En este punto iniciaré con las primeras configuraciones del proyecto y a medida que vaya avanzando iré actualizando

## para correr el proyecto
- inatalar dependencias `pip install -r requirements.txt`
- `python3 app/main.py` o `python app/main.py` en linux `py app/main.py` en windows
- para correr los tests usar `pytest -v`


### puntos de acceso api
- el servidor corre en la direccion http://localhost:5000
- el api se encuentra en la uri /api/v1/
- documentacion del api, se puede consultar en la direccion http://localhost:5000/apidocs
