

Group Members & Task Delegations:
    Bao, Roger            -   PART B
    Lagayada, Bea         -   PART B
    Laplap, Mariel        -   PART B
    Martinez, Thomas      -   PART A
    Ruelo, Cydney         -   PART A





Assessments:
1. Differentiate Task Parallelism and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.
   -   (a) Task Parallelism executes different functions concurrently on the same input.
    In task.py, four separate functions (compute_sss, compute_philhealth, compute_pagibig, compute_tax) are executed concurrently using ThreadPoolExecutor for one employee. The workload is divided by deduction type.

   -   (b) Data Parallelism applies the same function to multiple data elements simultaneously.
    In data.py, the single function compute_payroll() is applied to multiple employees using ProcessPoolExecutor. The workload is divided by employee.



2. Explain how concurrent.futures managed execution, including the roles of submit(), map(), and Future objects. Discuss the purpose of the with statement when creating an Executor.
   -   (a) In task.py:
        ThreadPoolExecutor creates worker threads.
        submit() schedules each deduction function.
        Each call returns a Future object.
        result() retrieves the computed value.
        The with statement ensures the thread pool is properly closed after execution.

   -   (b) In data.py:
        ProcessPoolExecutor creates multiple worker processes.
        map() distributes compute_payroll() across the employee list.
        Results are returned in order.
        The with statement ensures processes are properly started and terminated.



3. Analyze the execution of ThreadPoolExecutor in relation to the Global Interpreter Lock (GIL) and CPU cores. Did true parallelism occur? Explain your answer.
   -   (a) In task.py, ThreadPoolExecutor uses threads within a single process.
    Due to Python’s Global Interpreter Lock (GIL), only one thread executes Python bytecode at a time.
    Since deduction calculations are CPU-bound operations, true parallel execution across multiple CPU cores does not occur. The threads execute concurrently but not in true parallel CPU execution.



4. Explain why ProcessPoolExecutor enables true parallelism. Discuss memory space separation and GIL behavior.
   -   (b) In data.py, ProcessPoolExecutor creates separate processes. Each process:
        Has its own memory space
        Has its own Python interpreter
        Has its own GIL
    Because processes do not share a single GIL, multiple CPU cores can execute compute_payroll() simultaneously. The printed process_id demonstrates that different processes handled different employees, confirming true parallelism.



5. Evaluate the scalability of the system if the number of employees increases from 5 to 10,000. Which approach scales better and why?
   -   If employees increase to 10,000:

    (a) task.py (Task Parallelism) would not scale efficiently because it only parallelizes deductions within one employee at a time.
    (b) data.py (Data Parallelism) scales better because each employee’s payroll is independent and can be distributed across multiple processes and CPU cores.
    Therefore, the data-parallel approach in data.py is more scalable.


6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use for each case.
   -   In a real payroll system:
        (a) Task Parallelism (ThreadPoolExecutor)
        Used for independent operations on one employee, such as:
        Calculating deductions
        Generating payslips
        Logging payroll records

        (b) Data Parallelism (ProcessPoolExecutor)
        Used when processing payroll for thousands of employees simultaneously, where each employee’s computation is independent and CPU-intensive.
        The process-based approach is preferred for large-scale payroll computation because it enables true multi-core utilization.