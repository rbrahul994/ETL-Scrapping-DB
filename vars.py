import os

project_path = os.path.dirname(__file__)

transformed_data_path = project_path + "/data/transformed/"
log_path = project_path + "/logs/"

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks/'

exchange_rate = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'

target_file = 'Largest_banks_data.csv'

db_name = "Banks"

table_name = "Largest_banks"

log_file = "code_log.txt"