import json
from openbrewery import OpenBreweryAPI
from google.cloud import storage

# Define the Google Cloud Storage bucket name where the data will be stored
BUCKET = "abinbev-database-raw"

# Initialize the OpenBreweryAPI client to fetch brewery data
brewery_api = OpenBreweryAPI()

# Fetch a list of breweries as raw data from the OpenBrewery API
raw_data = brewery_api.get_breweries()

def write_file(json_list, bucket_name):
    """
    Function to upload a list of JSON objects to a Google Cloud Storage bucket.
    
    Args:
    json_list (list): List of JSON objects representing breweries.
    bucket_name (str): The name of the Google Cloud Storage bucket to upload files.
    """
    
    # Initialize the Google Cloud Storage client
    storage_client = storage.Client()
    
    # Get the bucket where the files will be uploaded
    bucket = storage_client.get_bucket(bucket_name)
    
    # Iterate over each JSON object in the list
    for json_file in json_list:
        
        # Extract the brewery ID from the JSON object to use as the file name
        brewery_id = json_file["id"]
        
        # Create a blob (file object) in the bucket with the brewery ID as the name
        blob = bucket.blob(brewery_id)
        
        # Upload the JSON object as a string to the bucket with content type set to JSON
        blob.upload_from_string(
            data=json.dumps(json_file),
            content_type='application/json'
        )
        
        # Print a message indicating the successful upload of the brewery
        print(brewery_id + ' upload complete')


if __name__ == "__main__":
    # Call the function to upload brewery data to the specified bucket
    write_file(raw_data, BUCKET)
