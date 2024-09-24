from pyspark.sql import SparkSession
from google.cloud import storage

# Change for GitHub Actions secrets
DELTA_LAKE  = "abinbev-database-delta-lake"  
BQ_TABLE    = "abinbev-case-eric:brewery_data.breweries" 
TEMP_BUCKET = "abinbev-temp" 

if __name__ == "__main__":
    # Create a Spark session with Delta Lake and BigQuery support
    spark = SparkSession.builder \
        .appName("ExportDeltaToBq") \
        .config("spark.jars.packages", "io.delta:delta-core_2.12:1.2.1,com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.26.0") \
        .getOrCreate()

    # Initialize Google Cloud Storage client
    client = storage.Client()
    bucket = client.get_bucket(DELTA_LAKE)  # Get the Delta Lake bucket

    # Set to hold unique Delta file paths
    delta_path = set()
    
    # Iterate over all blobs in the Delta Lake bucket
    for blob in bucket.list_blobs():
        # Create a path name using the first two components of the blob name
        path_name = "/".join(blob.name.split("/")[:2])
        # Add the unique Delta file path to the set
        delta_path.add(f"gs://{DELTA_LAKE}/{path_name}")

    # Read Delta files into a list of DataFrames
    delta_dfs = [spark.read.format("delta").load(path) for path in delta_path]

    # Initialize the combined DataFrame with the first Delta DataFrame
    combined_df = delta_dfs[0]

    # Union all subsequent DataFrames into the combined DataFrame
    for df in delta_dfs[1:]:
        combined_df = combined_df.unionByName(df)

    # Write the combined DataFrame to BigQuery
    combined_df.write \
        .format("bigquery") \
        .option("table", BQ_TABLE) \
        .option("temporaryGcsBucket", TEMP_BUCKET) \
        .mode("overwrite") \
        .save()  # Execute the write operation
