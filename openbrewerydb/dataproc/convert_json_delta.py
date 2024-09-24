import os

from pyspark.sql import SparkSession

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"

INPUT_BUCKET = "gs://abinbev-database-raw/"
OUTPUT_BUCKET = "gs://abinbev-database-delta-lake/"


if __name__ == "__main__":

    spark = SparkSession.builder \
        .appName("JSON to Delta Conversion") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.jars.packages", "io.delta:delta-core_2.13:2.3.0") \
        .config("spark.jars", "https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar") \
        .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
        .config("spark.hadoop.fs.gs.auth.service.account.enable", "true") \
        .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "key.json") \
        .getOrCreate()

    spark.conf.set("spark.sql.repl.eagerEval.enabled", True)

    json_df = spark.read.json(INPUT_BUCKET)

    for row in json_df.select("country", "state").distinct().collect():
        country = row["country"].lower().replace(" ", "_")
        state = row["state"].lower().replace(" ", "_")
        
        output_path = f"{OUTPUT_BUCKET}/{country}/{state}.delta"
            
        delta_output = json_df.filter((json_df.country == row["country"]) & (json_df.state == row["state"]))
        delta_output.write.format("delta").mode("overwrite").save(output_path)
        
        print(f"Saved data to: {output_path}")