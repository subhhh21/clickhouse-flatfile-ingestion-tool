from flask import Flask, render_template, request
from ingestion import ingest_clickhouse_to_file, ingest_file_to_clickhouse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.to_dict()
        if data['direction'] == "clickhouse_to_file":
            count = ingest_clickhouse_to_file(data)
        else:
            count = ingest_file_to_clickhouse(data)
        return f"<h2>{count} records processed successfully.</h2>"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
