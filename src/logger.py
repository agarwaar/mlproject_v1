import logging
import os
from datetime import datetime

# Create a 'logs' directory in the current working directory
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Create a log file with a timestamp in the filename
log_file = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"
log_path = os.path.join(log_dir, log_file)

# Set up logging
logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] [ %(levelname)s ] [%(module)s:%(lineno)d %(name)s] - %(message)s",
    level=logging.INFO  # Adjust the logging level as needed (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)
