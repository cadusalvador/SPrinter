import logging

logging.basicConfig(
    filename="SPrinter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(message):
    print(message)
    logging.info(message)