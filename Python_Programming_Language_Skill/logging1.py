import logging

logging.basicConfig(level=logging.DEBUG)

def process_data(x):
    logging.info(f"Processing value: {x}")
    if x < 0:
        logging.warning("Negative value detected")
    return x * 2

process_data(5)
process_data(-3)
