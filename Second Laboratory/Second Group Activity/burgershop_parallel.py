import time
import threading
import queue

NUM_ORDERS = 20

# Simulated processing times (seconds)
INTAKE_TIME = 0.2
PAYMENT_TIME = 0.2
COOK_TIME = 0.5
ASSEMBLE_TIME = 0.2
PACK_TIME = 0.1

def process_order_sequential(order):
    time.sleep(INTAKE_TIME)
    time.sleep(PAYMENT_TIME)
    time.sleep(COOK_TIME)
    time.sleep(ASSEMBLE_TIME)
    time.sleep(PACK_TIME)


def run_sequential(orders):
    start_time = time.time()

    for order in orders:
        process_order_sequential(order)

    end_time = time.time()
    return end_time - start_time

    