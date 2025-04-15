from clickhouse_client import fetch_data, upload_data
from flatfile_client import save_to_csv, load_from_csv

def ingest_clickhouse_to_file(config):
    rows, columns = fetch_data(config["host"], config["port"], config["database"], config["user"], config["token"])
    save_to_csv(rows, columns, config["filename"])
    return len(rows)

def ingest_file_to_clickhouse(config):
    df = load_from_csv(config["filename"])
    upload_data(config["host"], config["port"], config["database"], config["user"], config["token"], "new_table", df)
    return len(df)
