import os

PORT = 5000
HOST = "0.0.0.0"

api_version = "/v1"
hibp_breached_url = "https://haveibeenpwned.com/api/v3/breachedaccount/"
hibp_api_key = os.environ.get("HIBP_API_KEY")

postgres_hostname = os.environ.get("PGHOST", "postgres")
postgres_port = 5432
postgres_user = "admin"
postgres_password = os.environ.get("PGPASSWORD", "password")
db_name = "vuln_glance"

postgres_connection_string = f"postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_hostname}:{postgres_port}/{db_name}"

celery_broker = "amqp://vuln_glance:password@rabbitmq:5672/"