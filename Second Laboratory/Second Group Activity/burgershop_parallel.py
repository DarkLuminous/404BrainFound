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

