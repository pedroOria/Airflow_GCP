from google.cloud import bigquery

def query_bigquery():
    # Configura tu proyecto de GCP y autenticación
    client = bigquery.Client()

    # Define tu consulta
    query = """
        SELECT *
        FROM `proyect_1.weather_analysis.rain`
        LIMIT 10
    """

    # Ejecuta la consulta
    query_job = client.query(query)

    # Itera sobre los resultados
    for row in query_job:
        print(row)

if __name__ == "__main__":
    query_bigquery()