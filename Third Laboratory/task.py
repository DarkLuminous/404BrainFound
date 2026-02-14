employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

from concurrent.futures import ThreadPoolExecutor
import threading


# Deduction Functions (Now Showing Thread Name)

def compute_sss(salary):
    print(f"SSS computed by {threading.current_thread().name}")
    return salary * 0.045

def compute_philhealth(salary):
    print(f"PhilHealth computed by {threading.current_thread().name}")
    return salary * 0.025

def compute_pagibig(salary):
    print(f"Pag-IBIG computed by {threading.current_thread().name}")
    return salary * 0.02

def compute_tax(salary):
    print(f"Tax computed by {threading.current_thread().name}")
    return salary * 0.10


def task_parallel_payroll(employee):
    name, salary = employee

    print(f"\nProcessing payroll for {name} (Salary: {salary})\n")

    with ThreadPoolExecutor() as executor:
        future_sss = executor.submit(compute_sss, salary)
        future_philhealth = executor.submit(compute_philhealth, salary)
        future_pagibig = executor.submit(compute_pagibig, salary)
        future_tax = executor.submit(compute_tax, salary)

        sss = future_sss.result()
        philhealth = future_philhealth.result()
        pagibig = future_pagibig.result()
        tax = future_tax.result()

    total_deduction = sss + philhealth + pagibig + tax

    print("\n--- Deduction Breakdown ---")
    print(f"SSS: {sss:.2f}")
    print(f"PhilHealth: {philhealth:.2f}")
    print(f"Pag-IBIG: {pagibig:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Total Deduction: {total_deduction:.2f}")


# Run example (Charlie)
task_parallel_payroll(employees[0])
