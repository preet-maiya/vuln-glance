PORT = 5002
HOST = "0.0.0.0"
APP_NAME = "dataleaks"

api_version = "/v1"

## 3rd party api configs
api_hostname = "https://haveibeenpwned.com/"
all_breaches_endpoint = "api/v2/breaches"

## rabbitmq connection string
celery_broker = "amqp://guest:guest@localhost:5672/"

## cron configs
daily_fetch_time = 6
default_time = 1 # years

## db configs
psql_host = "localhost"
psql_user = "postgres"
psql_password = "postgres"
get_query = '''SELECT * from dataleaks where breach_epoch >= %s;'''
insert_data = f'''INSERT INTO dataleaks (breach_epoch, leak_info) values (%s, $$%s$$);'''
## create table command 
# create table dataleaks2 (leak_id serial primary key, breach_epoch integer not null, leak_info jsonb not null);