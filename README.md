
# Easy spark 

Contenedores docker de Spark basados en debian:buster, desarrollados originalmente por [Gettyimages](https://www.github.com/gettyimages).
Esta versión está actualizada a Python 3.10 y Spark 3.4.4. Pensado para desplegar de forma local y sencilla en un entorno de desarrollo.

# Importante

Spark y PySpark son muy sensibles a las versiones de las librerías que se usan. 
Para que funcione adecuadamente, es necesario Python `3.10`, y la versión `3.4.4` de `pyspark`.

Para crear un entorno de python rápidamente con conda:
```bash
conda create -y -n pyspark python=3.10
conda activate pyspark
pip install -r requirements.txt
```

# Despliegue en docker local

Primero, instalar docker-compose, si no viene por defecto en tu instalación de docker:

```bash
sudo apt install docker-compose
```

Después, arrancar todos los servicios con:

```bash
docker-compose up
```

Para arrancar los servicios en background:

```bash
docker-compose up -d
```

Para pararlo todo:

```bash
docker-compose down
```

# Interfaz de Spark master

Podemos ver la interfaz del nodo maestro de spark en [http://localhost:8080](http://localhost:8080).

Deberían aparecer tres workers con state `ALIVE`.

# Lanzar tareas de ejemplo en el cluster de spark creado

Entramos en el contenedor con `bash`:

```bash
docker exec -it docker-spark_master_1 /bin/bash
```

Una vez dentro, para lanzar un trabajo de ejemplo:

```bash
bin/run-example SparkPi 10
```

Mientras se completa, podremos ver en la interfaz web del nodo maestro la aplicación en curso. Cuando finalice, aparecerá en la lista de aplicaciones completadas.

# Conexión con PySpark

En `pyspark_example.py` se encuentra un ejemplo de cómo conectarse al cluster y crear un dataframe. Con el entorno de python `3.7` activado, ejecutar:

```bash
python pyspark_example.py
```

## License

MIT
