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

#Sequential Version
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


# Parallel Version
def worker_intake(input_queue, cooking_queue):
    while True:
        order = input_queue.get()
        if order is None:
            break

        time.sleep(INTAKE_TIME)
        time.sleep(PAYMENT_TIME)

        cooking_queue.put(order)
        input_queue.task_done()


def worker_cooking(cooking_queue, assembly_queue, grill_lock):
    while True:
        order = cooking_queue.get()
        if order is None:
            break

        # Critical Section (Shared Grill)
        with grill_lock:
            time.sleep(COOK_TIME)

        assembly_queue.put(order)
        cooking_queue.task_done()

def worker_assembly(assembly_queue):
    while True:
        order = assembly_queue.get()
        if order is None:
            break

        time.sleep(ASSEMBLE_TIME)
        time.sleep(PACK_TIME)

        assembly_queue.task_done()

