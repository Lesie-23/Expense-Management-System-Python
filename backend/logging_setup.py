import logging
import os

def setup_logger(name, log_file='server.log', level=logging.DEBUG):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    # Get the folder where this file (db_helper.py) lives
    module_dir = os.path.dirname(os.path.abspath(__file__))

    # Build log path inside backend folder relative to this module
    log_path = os.path.join(module_dir, log_file)

    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.propagate = False

    return logger