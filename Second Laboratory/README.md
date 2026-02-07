# Second Laboratory – Exploring Multithreading and Multiprocessing in Python

## Group Members
- Bao, Roger  
- Lagayada, Bea  
- Laplap, Mariel  
- Martinez, Thomas  
- Ruelo, Cydney  

---

## Objective
This laboratory activity explores the use of **multithreading** and **multiprocessing** in Python by implementing a Grade Computing System. Users can input grades manually or generate large datasets, and the system computes the General Weighted Average (GWA) while comparing execution behavior and performance between the two concurrency approaches.

---

## How to Run the Program
```bash
python main.py


| Method          | Execution Order   | GWA Output | Execution Time |
| --------------- | ----------------- | ---------- | -------------- |
| Multithreading  | Non-deterministic | Correct    | ~0.15 seconds  |
| Multiprocessing | Non-deterministic | Correct    | ~1.38 seconds  |


Discussion

The output order of both multithreading and multiprocessing is non-deterministic because the operating system controls how threads and processes are scheduled. The OS dynamically allocates CPU time, which can change between executions, resulting in different output orders and execution times.

Multithreading generally performs better for small or I/O-bound tasks due to its lower overhead and shared memory space. Multiprocessing introduces additional overhead from process creation and memory separation, but it enables true parallel execution and is more suitable for CPU-bound workloads. Code readability and performance analysis were improved by using modular design, class-based structure, and summarized output for large datasets.


Questions and Answers

1. Which approach demonstrates true parallelism in Python? Explain.

    Multiprocessing demonstrates true parallelism in Python. Each process runs independently with its own memory space and can execute on a separate CPU core. Because processes are not restricted by Python’s Global Interpreter Lock (GIL), multiple computations can actually happen at the same time, especially on multi-core systems.


2. Compare execution times between multithreading and multiprocessing.

    Based on our observations, multithreading often finishes faster for small or lightweight tasks because it has lower overhead. However, when tasks become more computationally heavy, multiprocessing tends to perform better. This is because multiprocessing allows the workload to be distributed across multiple CPU cores, while multithreading is limited to a single core due to the GIL.

    
3. Can Python handle true parallelism using threads? Why or why not?

    Python cannot achieve true parallelism using threads for CPU-bound tasks. This is mainly because of the Global Interpreter Lock, which allows only one thread to execute Python bytecode at a time. Although threads can run concurrently, they do not execute in parallel when performing heavy computations.
    
4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?

    When a large number of grades (e.g., 1000) is input, multiprocessing performs better than multithreading. Multithreading is limited by Python’s Global Interpreter Lock (GIL), which prevents true parallel execution and adds overhead as threads increase. Multiprocessing avoids this limitation by using multiple processes across CPU cores, making it faster for large workloads despite slightly higher startup costs.

5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?
    For CPU-bound tasks that involve heavy computation, multiprocessing works better because it can run tasks in parallel across multiple CPU cores and is not limited by the GIL. On the other hand, multithreading is more suitable for I/O-bound tasks since while one thread is waiting for input or data, other threads can continue running, making more efficient use of waiting time.

6. How did your group apply creative coding or algorithmic solutions in this lab?

    Our group applied creative coding by designing a menu-driven system that allows users to input grades manually or generate large datasets for testing. We implemented class-based and modular programming to improve code readability and organization. We also added execution time measurement, automated performance comparison, and structured output formatting to clearly analyze the differences between multithreading and multiprocessing.