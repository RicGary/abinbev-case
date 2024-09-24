import os
from pyspark.sql import SparkSession

# Set the environment variable for Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"

# Define input and output bucket paths for Google Cloud Storage
INPUT_BUCKET = "gs://abinbev-database-raw/"
OUTPUT_BUCKET = "gs://abinbev-database-delta-lake/"

if __name__ == "__main__":

    # Create a Spark session with Delta Lake support and Google Cloud Storage configuration
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

    # Enable eager evaluation for better readability of DataFrame outputs in the REPL
    spark.conf.set("spark.sql.repl.eagerEval.enabled", True)

    # Read JSON data from the input bucket into a DataFrame
    json_df = spark.read.json(INPUT_BUCKET)

    # Iterate over distinct combinations of country and state from the DataFrame
    for row in json_df.select("country", "state").distinct().collect():
        # Format country and state names for the output path
        country = row["country"].lower().replace(" ", "_")
        state = row["state"].lower().replace(" ", "_")
        
        # Define the output path for the Delta file
        output_path = f"{OUTPUT_BUCKET}/{country}/{state}.delta"
        
        # Filter the DataFrame for the current country and state
        delta_output = json_df.filter((json_df.country == row["country"]) & (json_df.state == row["state"]))
        
        # Write the filtered DataFrame to the specified output path in Delta format
        delta_output.write.format("delta").mode("overwrite").save(output_path)
        
        # Print a message indicating where the data has been saved
        print(f"Saved data to: {output_path}")
