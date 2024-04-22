from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .appName("MiAplicacionSpark") \
        .master("spark://localhost:7077") \
        .getOrCreate()

try:
    # Ejemplo de cómo realizar una operación simple: crear un DataFrame y mostrarlo
    data = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
    columns = ["Language", "Users"]

    df = spark.createDataFrame(data, schema=columns)
    df.show()
except Exception as e:
    print(f"Error al procesar datos con Spark: {e}")
finally:
    spark.stop()