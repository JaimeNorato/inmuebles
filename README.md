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
- ejecuta `cp .env_example .env` o copia, pega y renombra el archivo `.env_example` por `.env` y agrega los varoles de las variables de entorno
- `python3 app/main.py` o `python app/main.py` en linux `py app/main.py` en windows
- para correr los tests usar `pytest -v`


### puntos de acceso api
- El servidor corre en la dirección http://localhost:5000
- el api se encuentra en la uri ==/api/v1/==
- documentacion del api, se puede consultar en la direccion http://localhost:5000/apidocs
- Se incluye un .json que se puede importar en insomnia o compatibles, el cual contiene los request con los que se puede realizar pruebas del api, el archivo se llama ==Insomnia_test_api.json== el cual se encuentra en la raíz de este proyecto

### Extensión para favoritos 
Para agregar la funcionalidad de inmuebles favoritos, se crea una tabla pívot o de relación muchos a muchos, llamada `property_favorites_user`, esta tabla contiene los cambos `user_id` y `property_id` los cuales son llaves primarias que hacen referencias a los `id` de auth_property u property respectivamente.

Se eligió una tabla pívot, ya que un usuario agrega a un inmueble específico a favoritos una sola vez, y no se requiere que lo esté agregando más de una vez, a su vez de esta forma se puede listar de forma rápida los inmuebles que tiene en favoritos el usuario y así mismo se pueden ver qué usuarios o cuantos usuarios han agregado a favoritos un inmueble en específico 

#### Para extender la BD
Se agrega un archivo llamado `favorites.sql` que se encuentra en la raíz del proyecto donde se encuentra los scripts necesarios para crear y consultar la nueva tabla