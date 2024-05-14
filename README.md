# Proyecto de Análisis Meteorológico con Apache Airflow y GCP

Este proyecto utiliza Apache Airflow en Google Cloud Platform (GCP) para orquestar el análisis de datos meteorológicos históricos. El objetivo es procesar los datos almacenados en BigQuery y generar un informe de tendencias climáticas mensuales.

## Estructura del Proyecto

El proyecto sigue la siguiente estructura de directorios:

- **dags/**: Contiene el DAG de Airflow para orquestar el flujo de trabajo.
- **scripts/**: Contiene los scripts Python para procesar los datos.
- **README.md**: Este archivo que proporciona información sobre el proyecto.

## Configuración

1. **Configuración de GCP**: Asegúrate de tener una cuenta de GCP y haber configurado un proyecto. Habilita los servicios de Google Cloud Composer y BigQuery.
2. **Instalación de Dependencias**: Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
3. **Configuración de Variables de Entorno**: Define las variables de entorno necesarias para la conexión con GCP y otras configuraciones en tu entorno de Airflow.
4. **Ejecución del DAG**: Inicia el DAG `weather_analysis.py` en tu entorno de Airflow.

## Uso

1. Clona este repositorio en tu entorno local.
2. Configura las variables de entorno necesarias.
3. Instala las dependencias ejecutando `pip install -r requirements.txt`.
4. Inicia el DAG `weather_analysis.py` en tu entorno de Airflow.

## Contribuciones

¡Siéntete libre de contribuir con mejoras o nuevas características! Abre un pull request para discutir los cambios propuestos.

## Autores

- [Pedro Oria](https://github.com/pedroOria) - Desarrollador principal


