from concurrent.futures import ProcessPoolExecutor
import os

# Deduction rates
SSS_RATE = 0.045
PHILHEALTH_RATE = 0.025
PAGIBIG_RATE = 0.02
TAX_RATE = 0.10

# Given employees
employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

# Function to compute payroll for one employee
def compute_payroll(employee):
    name, salary = employee

    # Individual deductions
    sss = salary * SSS_RATE
    philhealth = salary * PHILHEALTH_RATE
    pagibig = salary * PAGIBIG_RATE
    tax = salary * TAX_RATE

    # Total deduction
    total_deduction = sss + philhealth + pagibig + tax

    # Net salary
    net_salary = salary - total_deduction

    # Optional: show process ID to demonstrate multiprocessing
    process_id = os.getpid()

    return {
        "name": name,
        "salary": salary,
        "sss": sss,
        "philhealth": philhealth,
        "pagibig": pagibig,
        "tax": tax,
        "total_deduction": total_deduction,
        "net_salary": net_salary,
        "process_id": process_id
    }

def main():
    print("=== Data Parallelism: Payroll Computation ===\n")

    # Process Pool Executor
    with ProcessPoolExecutor() as executor:

        # Compute_payroll to all employees in parallel
        results = executor.map(compute_payroll, employees)

        # Results
        for result in results:
            print(f"Process ID: {result['process_id']}")
            print(f"Employee Name: {result['name']}")
            print(f"Gross Salary: {result['salary']:.2f}")

            print("Deductions:")
            print(f"  SSS: {result['sss']:.2f}")
            print(f"  PhilHealth: {result['philhealth']:.2f}")
            print(f"  Pag-IBIG: {result['pagibig']:.2f}")
            print(f"  Withholding Tax: {result['tax']:.2f}")

            print(f"Total Deduction: {result['total_deduction']:.2f}")
            print(f"Net Salary: {result['net_salary']:.2f}")
            print("-" * 40)


# Required for multiprocessing
if __name__ == "__main__":
    main()
