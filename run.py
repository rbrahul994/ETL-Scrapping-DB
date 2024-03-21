#
from etl_logger import log_progress
from code.extract_data import extract
from code.transform import transform
from code.load import load_to_csv, load_to_db
from code.queries import sql_queries
from vars import target_file 


# Log the initialization of the ETL process
log_progress("ETL Job Started")
 
# Log the beginning of the Extraction process
log_progress("Extract phase Started")
extracted_data, exchange_rate_df = extract() 

# Log the completion of the Extraction process
log_progress("Extract phase Ended")
 
# Log the beginning of the Transformation process
log_progress("Transform phase Started")
transformed_data = transform(extracted_data, exchange_rate_df)

print("Transformed Data") 
print(transformed_data)

# Log the completion of the Transformation process
log_progress("Transform phase Ended")
 
# Log the beginning of the Loading process
log_progress("Load phase Started")
load_to_csv(target_file, transformed_data)

load_to_db(transformed_data) 

# Log the completion of the Loading process
log_progress("Load phase Ended")

log_progress("Running Queries on Database")
sql_queries()
log_progress("Exiting Database")
 
# Log the completion of the ETL process
log_progress("ETL Job Ended")