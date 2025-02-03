import os
from google.cloud import storage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = “Path of the json key file"
client = storage.Client()
bucket = client.get_bucket(“bucket name")
blob = bucket.blob("backup file name.bak")
blob.upload_from_filename(“backup file path")
