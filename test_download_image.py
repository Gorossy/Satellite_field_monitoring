import responses
import pytest
from index import download_image
from moto import mock_s3
import boto3
import requests_mock
import os
import csv

def load_settings():
    settings = {
        "api_key": os.environ['NASA_API_KEY'],
        "bucket_name": os.environ['BUCKET_NAME'],
        "aws_access_key_id": os.environ['AWS_ACCESS_KEY_ID'],
        "aws_secret_access_key": os.environ['AWS_SECRET_ACCESS_KEY'],
        "date": os.environ['DATE']
    }
    return settings
settings = load_settings()
field = {
    'lat': 29.78,
    'lon': -95.33,
    'dim': 0.10,
    'field_id': 'test_field'
}
lon = field['lon']
lat = field['lat']
dim = field['dim']
api_key = settings['api_key']
date = settings['date']
url_to_mock = f"https://api.nasa.gov/planetary/earth/imagery?lon={lon}&lat={lat}&dim={dim}&date={date}&api_key={api_key}"

# Define una respuesta ficticia para esa URL
mock_response_content = b"fake_image_content"

# Define un diccionario con los datos de un campo
field = {
    'lat': 29.78,
    'lon': -95.33,
    'dim': 0.10,
    'field_id': 'test_field'
}

s3_client = boto3.client('s3', region_name='us-east-1')
bucket_name = "test-bucket"


@mock_s3
def test_download_image(requests_mock):
    # Crea un bucket falso en S3
    s3_client.create_bucket(Bucket=bucket_name)

    # Registra la URL con la respuesta ficticia
    requests_mock.get(url_to_mock, content=mock_response_content)

    # Llama a la función que quieres probar (no es necesario pasar una sesión)
    download_image(date, field, api_key, s3_client, bucket_name)

    # Verifica que la imagen se haya almacenado en S3
    response = s3_client.get_object(Bucket=bucket_name, Key=f"{field['field_id']}/{date}_imagery.png")
    assert response['Body'].read() == mock_response_content
