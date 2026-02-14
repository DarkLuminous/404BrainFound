employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

def compute_sss(salary):
    return salary * 0.045

def compute_philhealth(salary):
    return salary * 0.025

def compute_pagibig(salary):
    return salary * 0.02

def compute_tax(salary):
    return salary * 0.10

from concurrent.futures import ThreadPoolExecutor
import threading

def task_parallel_payroll(employee):
    name, salary = employee
    
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

    print(f"\nEmployee: {name}")
    print(f"SSS: {sss}")
    print(f"PhilHealth: {philhealth}")
    print(f"Pag-IBIG: {pagibig}")
    print(f"Tax: {tax}")
    print(f"Total Deduction: {total_deduction}")

task_parallel_payroll(employees[2])