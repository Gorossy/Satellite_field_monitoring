import boto3
import csv
import requests
from concurrent.futures import ThreadPoolExecutor
from moto import mock_s3
import os

def load_settings():
    settings = {
        "api_key": os.environ['NASA_API_KEY'],
        "bucket_name": os.environ['BUCKET_NAME'],
        "aws_access_key_id": os.environ['AWS_ACCESS_KEY_ID'],
        "aws_secret_access_key": os.environ['AWS_SECRET_ACCESS_KEY'],
        "date": os.environ['DATE']
    }
    return settings

def load_fields_from_csv(file_path):
    fields = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            fields.append(row)
    return fields

def download_image(date, field, api_key, s3_client, bucket_name):
    lat = field['lat']
    lon = field['lon']
    dim = field['dim']
    url = f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&dim={dim}&date={date}&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        key = f"{field['field_id']}/{date}_imagery.png"
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=response.content)

@mock_s3
def main():
    settings = load_settings()
    s3_client = boto3.client('s3', region_name='us-east-1', aws_access_key_id=settings["aws_access_key_id"], aws_secret_access_key=settings["aws_secret_access_key"])
    bucket_name = settings["bucket_name"]
    s3_client.create_bucket(Bucket=bucket_name)

    fields = load_fields_from_csv('fields.csv')
    api_key = settings['api_key']
    date = settings['date']

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_image, date, field, api_key, s3_client, bucket_name) for field in fields]
        for future in futures:
            future.result()

if __name__ == '__main__':
    main()
