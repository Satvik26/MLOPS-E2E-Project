import os
import sys
import logging
 
logging_str = "%(levelname)s : (%(asctime)s) : %(message)s : (Line : %(lineno)d) [%(filename)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)
 
if os.path.exists(log_filepath):
    # If it exists, append a newline before logging
    with open(log_filepath, 'a') as log_file:
        log_file.write('\n')
 
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
 
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
 
logger = logging.getLogger("Reporting \n" )