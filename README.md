README.md
markdown
Copy
Edit
# ClickHouse & Flat File Data Ingestion Tool

This is a Python-based web application to ingest data between ClickHouse and flat files (CSV). It supports bidirectional data transfer, a user-friendly frontend, JWT-based authentication, and status reporting.

---

## 🚀 Features

- 🔄 **Bidirectional Data Ingestion**
  - ClickHouse → Flat File
  - Flat File → ClickHouse
- 👤 JWT Authentication
- 📋 Column selection via UI
- 🖥 Web interface to manage configurations
- 📈 Record count reporting after ingestion

---

## 🧰 Requirements

- Python 3.7 or higher
- Docker (for running ClickHouse)
- Flask (Web Framework)
- clickhouse-connect (Client Library)
- Other packages listed in `requirements.txt`

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/subhhh21/clickhouse-flatfile-ingestion-tool.git
cd clickhouse-flatfile-ingestion-tool
2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
# For Linux/macOS
source venv/bin/activate
# For Windows
venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run ClickHouse with Docker
bash
Copy
Edit
docker run -d --name clickhouse-server -p 8123:8123 -p 9000:9000 clickhouse/clickhouse-server
5. Configure the App
Update config.py with your ClickHouse and JWT settings:

python
Copy
Edit
CLICKHOUSE_HOST = 'localhost'
CLICKHOUSE_PORT = 8123
CLICKHOUSE_USER = 'default'
CLICKHOUSE_PASSWORD = 'password'
JWT_SECRET_KEY = 'your-secret-key'
6. Run the Application
bash
Copy
Edit
python main.py
App will start at http://127.0.0.1:5000

🌐 Using the App
Go to http://127.0.0.1:5000

Choose source: ClickHouse or Flat File

Fill in connection details

Load & select columns

Click "Start Ingestion"

View record count after completion

🧪 Testing Scenarios
✅ ClickHouse to Flat File

✅ Flat File to ClickHouse

✅ Auth failures with JWT

✅ UI status updates and error reporting

🛠 Troubleshooting
Error 500: Check logs in terminal.

Connection refused: Ensure Docker container is running.

File read errors: Verify CSV file format and path.

📦 requirements.txt
txt
Copy
Edit
Flask==2.1.0
clickhouse-connect==0.3.2
pyjwt==2.4.0
