# Satellite field monitoring
Este proyecto realiza la descarga de imágenes satelitales de la Tierra utilizando la API de la NASA. Las coordenadas geográficas y los parámetros para las imágenes se extraen de un archivo CSV, y las imágenes descargadas se almacenan en un bucket de Amazon S3.

## **Características Principales**

- **Descarga Dinámica**: Utiliza las coordenadas y parámetros especificados en un archivo CSV para descargar imágenes a través de la API de la NASA.
- **Almacenamiento en S3**: Las imágenes descargadas se guardan en un bucket de Amazon S3, organizadas por fechas y campos.
- **Pruebas Automatizadas**: Incluye pruebas unitarias para garantizar que la descarga y el almacenamiento se realicen correctamente.
- **Paralelización**: Utiliza el módulo `concurrent.futures` para realizar descargas paralelas, mejorando la eficiencia en la obtención de múltiples imágenes.
