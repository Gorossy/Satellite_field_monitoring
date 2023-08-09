# Satellite field monitoring
Este proyecto realiza la descarga de imágenes satelitales de la Tierra utilizando la API de la NASA. Las coordenadas geográficas y los parámetros para las imágenes se extraen de un archivo CSV, y las imágenes descargadas se almacenan en un bucket de Amazon S3.

## **Características Principales**

- **Descarga Dinámica**: Utiliza las coordenadas y parámetros especificados en un archivo CSV para descargar imágenes a través de la API de la NASA.
- **Almacenamiento en S3**: Las imágenes descargadas se guardan en un bucket de Amazon S3, organizadas por fechas y campos.
- **Pruebas Automatizadas**: Incluye pruebas unitarias para garantizar que la descarga y el almacenamiento se realicen correctamente.
- **Paralelización**: Utiliza el módulo `concurrent.futures` para realizar descargas paralelas, mejorando la eficiencia en la obtención de múltiples imágenes.

## **Uso**

Este proyecto está diseñado para ejecutarse en un contenedor Docker, lo que facilita la configuración y despliegue.

### **Preparación**

1. **Clonar el Repositorio**: Clone este repositorio en su máquina local utilizando `git clone <URL_DEL_REPOSITORIO>`.

2. **Configurar Variables de Entorno**: Abra el archivo `Dockerfile` y ajuste las siguientes variables de entorno según su configuración:

   - `ENV NASA_API_KEY=<Apikey>`: Reemplace `<Apikey>` con su clave API proporcionada por la NASA.
   - `ENV BUCKET_NAME=<bucket-name>`: Reemplace `<bucket-name>` con el nombre del bucket de Amazon S3 donde se almacenarán las imágenes.
   - `ENV AWS_ACCESS_KEY_ID=<access-key>`: Reemplace `<access-key>` con su clave de acceso AWS.
   - `ENV AWS_SECRET_ACCESS_KEY=<secret-key>`: Reemplace `<secret-key>` con su clave secreta AWS.
   - `ENV DATE=<fecha>`: Reemplace `<fecha>` con la fecha de las imágenes que desea descargar.

### **Construir la Imagen Docker**

Desde el directorio donde se encuentra el archivo `Dockerfile`, ejecute el siguiente comando para construir la imagen Docker:

```bash
docker build -t nombre_de_la_imagen .
docker run nombre_de_la_imagen
docker run nombre_de_la_imagen pytest

