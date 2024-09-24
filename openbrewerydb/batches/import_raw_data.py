import json

from openbrewery import OpenBreweryAPI

from google.cloud import storage

BUCKET = "abinbev-database-raw"

brewery_api = OpenBreweryAPI()
raw_data = brewery_api.get_breweries()

def write_file(json_list, bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    for json_file in json_list:

        brewery_id = json_file["id"]
        blob = bucket.blob(brewery_id)
        blob.upload_from_string(
            data=json.dumps(json_file),
            content_type='application/json'
        )

        print(brewery_id + ' upload complete')


if __name__ == "__main__":
    write_file(raw_data, BUCKET)
    