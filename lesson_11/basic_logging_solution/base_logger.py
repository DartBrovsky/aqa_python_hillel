import logging

logging.basicConfig(filename='example.log', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
logging.getLogger("").addHandler(console_handler)


logging.info("First Initial Logging")
logging.warning("First Initial Warning logging")
