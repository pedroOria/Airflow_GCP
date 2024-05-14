from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Importa la función de procesamiento de datos desde data_processing.py
from scripts.data_processing import query_bigquery

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 13),
    'retries': 1
}

# Define la función que será ejecutada como tarea
def process_weather_data():
    query_bigquery()

# Define el DAG
with DAG('weather_analysis', 
         default_args=default_args, 
         schedule_interval='@daily', 
         catchup=False) as dag:

    # Define la tarea que ejecuta el procesamiento de datos
    process_weather_task = PythonOperator(
        task_id='process_weather_data_task',
        python_callable=process_weather_data
    )

    # Establece la secuencia de tareas
    process_weather_task
