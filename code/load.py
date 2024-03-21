#
import sqlite3
import pandas as pd

from vars import transformed_data_path, table_name, db_name


def load_to_csv(target_file, transformed_data): 
    transformed_data.to_csv(transformed_data_path + target_file) 
    return None

def load_to_db(transformed_data):
    conn = sqlite3.connect(db_name)
    transformed_data.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.close()
    return None