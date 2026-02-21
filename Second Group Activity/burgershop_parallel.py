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

def run_parallel(orders):
    input_queue = queue.Queue()
    cooking_queue = queue.Queue()
    assembly_queue = queue.Queue()

    grill_lock = threading.Lock()

    # Start timer
    start_time = time.time()

    # Create threads
    t1 = threading.Thread(target=worker_intake, args=(input_queue, cooking_queue))
    t2 = threading.Thread(target=worker_cooking, args=(cooking_queue, assembly_queue, grill_lock))
    t3 = threading.Thread(target=worker_assembly, args=(assembly_queue,))

    t1.start()
    t2.start()
    t3.start()

    # Put orders into input queue
    for order in orders:
        input_queue.put(order)

    # Wait for all orders to be processed
    input_queue.join()
    cooking_queue.join()
    assembly_queue.join()

    # Stop workers
    input_queue.put(None)
    cooking_queue.put(None)
    assembly_queue.put(None)

    t1.join()
    t2.join()
    t3.join()

    end_time = time.time()
    return end_time - start_time

# Main Benchmark
if __name__ == "__main__":
    orders = [Order(i) for i in range(NUM_ORDERS)]

    print("Running Sequential Version...")
    sequential_time = run_sequential(orders)
    print(f"Sequential Time: {sequential_time:.4f} seconds")

    print("\nRunning Parallel Version...")
    parallel_time = run_parallel(orders)
    print(f"Parallel Time: {parallel_time:.4f} seconds")

    speedup = sequential_time / parallel_time
    print(f"\nSpeedup: {speedup:.2f}x")
    