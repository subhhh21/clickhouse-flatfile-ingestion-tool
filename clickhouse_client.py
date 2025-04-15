from clickhouse_connect import get_client

def fetch_data(host, port, database, username, token):
    client = get_client(host=host, port=int(port), username=username, password=token, database=database)
    result = client.query("SELECT * FROM your_table LIMIT 100")
    return result.result_rows, result.column_names

def upload_data(host, port, database, username, token, table_name, df):
    client = get_client(host=host, port=int(port), username=username, password=token, database=database)
    client.insert_df(table_name, df)

