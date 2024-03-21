#
from datetime import datetime
from vars import log_path, log_file

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open(log_path + log_file, "a") as f:
        f.write(timestamp + ', ' + message + '\n')
    return None


