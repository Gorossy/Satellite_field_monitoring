FROM python:3.8-slim

WORKDIR /app

# Definición de las variables de entorno con valores
ENV NASA_API_KEY=<Apikey>
ENV BUCKET_NAME=<bucket-name>
ENV AWS_ACCESS_KEY_ID=<access-key>
ENV AWS_SECRET_ACCESS_KEY=<secret-key>
ENV DATE=<fecha>

# Copiar los archivos necesarios al contenedor
COPY . /app
WORKDIR /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt
