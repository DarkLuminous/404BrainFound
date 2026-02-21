# Real-World Bottleneck: Sequential Service in a Burger Shop

**Team Name:** Huntrix Group  
**Date:** February 21, 2026  
**Members:** Bao, Lagayada, Laplap, Martinez, Ruelo

---

## Problem Description

In a typical small Burger Shop, especially during non-peak staffing hours, a single crew member is responsible for handling the entire order fulfillment process. This includes:

- Taking customer orders
- Processing payment
- Preparing the burger (grilling the patty and toasting the bun)
- Assembling the ingredients
- Packing the order
- Handing it to the customer

All these tasks are performed **sequentially** for one customer before the next order is started.

The primary bottleneck is the **single-worker sequential workflow**. Because only one person executes all stages of service, no overlap between tasks is possible. For example, while the patty is cooking, the worker cannot simultaneously take another order or begin preparing a second burger. This results in:

- Idle resource time (e.g., grill cooking time not being used to process another order)
- Increased customer waiting time, especially during peak hours

This bottleneck limits overall efficiency because system throughput is constrained by the total time required to complete one full order cycle. If one order takes approximately four minutes, the maximum output is roughly **15 orders per hour**. As customer arrival rates increase beyond this capacity, queues form quickly, leading to long wait times and potential loss of sales.

The inefficiency does not stem from slow individual tasks, but rather from the **strictly sequential structure** of the workflow. The system lacks task distribution, meaning that independent activities (such as cooking and order-taking) cannot occur simultaneously even though they do not logically depend on one another. Therefore, the bottleneck is **structural rather than procedural**, making it a strong candidate for optimization through parallelization.

---

## Computational Mapping (From Physical to Digital Model)

To analyze the identified bottleneck, the real-world workflow is translated into a computational model using Parallel and Distributed Computing (PDC) principles.

### 1. Definition of the Work Unit

The fundamental unit of computation is defined as:

> **One burger order**

Each order represents a single independent task that must pass through multiple processing stages. In computational terms, an order is a data structure containing:

- Order ID
- Order intake time
- Payment processing time
- Cooking time
- Assembly time
- Packaging time

Multiple orders represent multiple work units that can potentially be processed concurrently.

### 2. Sequential Computational Model

In the current real-world setup, the system operates as a **single-threaded processor**. One worker performs all stages of service sequentially before beginning the next order.

**Algorithm:**
```
For each order in the list of incoming orders:
  1. Process order intake
  2. Process payment
  3. Cook the patty
  4. Assemble the burger
  5. Pack the order
```

The total execution time is expressed as:

```
Total Sequential Time = N × T_total_per_order

where:
  T_total_per_order = T_intake + T_payment + T_cook + T_assemble + T_pack
```

This results in **strictly linear scaling** — no overlap exists between tasks, and throughput is limited by the full completion time of each order.

### 3. Parallel Computational Model

To reduce the bottleneck, the workflow is reorganized into a **pipeline-based parallel system** with specialized worker nodes:

| Worker | Responsibility |
|--------|---------------|
| Worker 1 | Order intake and payment |
| Worker 2 | Cooking |
| Worker 3 | Assembly and packaging |

Each worker executes a different stage concurrently. Orders move through the system using **queues** between stages. This allows multiple orders to be processed simultaneously:

- Order A → cooking stage
- Order B → payment stage
- Order C → assembly stage

This reduces idle time and increases throughput.

### 4. System Constraints and Scalability Limits

Parallelism is not unlimited. Several constraints affect scalability:

**a. Critical Sections (Shared Resources)**  
The grill is a shared resource. If multiple threads attempt to cook patties simultaneously, synchronization mechanisms (e.g., **locks/mutexes**) are required to prevent conflicts.

**b. Task Dependencies**  
Within each order, stages must occur in sequence:
- Assembly cannot begin before cooking finishes
- Packaging cannot begin before assembly completes

These dependencies require synchronization between pipeline stages.

**c. Resource Contention**  
If the number of incoming orders exceeds the capacity of a stage (e.g., cooking takes longer than payment), that stage becomes the **new bottleneck**.

---

## Chosen Parallel Strategy: Task Parallelism (Pipeline Model)

The burger shop bottleneck maps directly to **Task Parallelism** because each stage of order fulfillment is a distinct operation — not the same operation repeated on different data. The four stages are:

1. **Take Order** — order interaction
2. **Grill Patty** — cooking
3. **Assemble & Pack** — food preparation
4. **Collect Payment** — transaction processing

These are fundamentally different tasks, which is the defining characteristic of task parallelism. This is in contrast to **data parallelism**, where the same operation (e.g., grilling) would be applied to multiple patties simultaneously across parallel workers.

---

## Flowcharts

### Sequential Workflow

```
         [START]
            |
     [Take Order]
            |
  [Process Payment]
            |
   [Cook Patty 🔒]
            |
  [Assemble Burger]
            |
    [Pack Order]
            |
          [END]
```

This diagram illustrates the original sequential workflow where a single processing unit handles all tasks from start to finish. Each stage is executed one after another — no stage begins until the previous one has fully completed. This represents a **single-threaded computational model** where total execution time increases linearly with the number of orders.

---

### Parallel Pipeline Workflow

```
[Incoming Orders]
       |
  [Input Queue]
       |
  [Worker 1: Intake & Payment]
       |
   [Queue 1]
       |
  [Worker 2: Cooking 🔒 (Grill Lock)]
       |
   [Queue 2]
       |
  [Worker 3: Assembly & Packaging]
       |
   [COMPLETE]
```

This diagram represents the redesigned system using **pipeline-based task parallelism**. Incoming orders are placed in an input queue and distributed to independent worker threads. Worker 2 includes a **critical section** representing shared grill access that requires synchronization. Multiple orders can be processed simultaneously at different stages — increasing throughput while maintaining order integrity.

---

## Benchmark Report

The purpose of this benchmark is to evaluate the performance improvement achieved by applying Task Parallelism to the burger shop system.

### Test Configuration

- **Total orders:** 20
- **Tasks per order:** Order taking, Payment processing, Cooking, Assembly, Packing
- **Parallel implementation:**
  - Thread 1 → Cashier (Intake & Payment)
  - Thread 2 → Cook (Grilling)
  - Thread 3 → Packer (Assembly & Packaging)
- **Shared resources:** Grill (mutex protected), Cash register (mutex protected)

Execution time was measured from the moment processing started until all orders were completed.

### Results

| Model | Execution Time |
|-------|---------------|
| Sequential | 24.02 seconds |
| Parallel | 10.13 seconds |

### Speedup Calculation

```
Speedup = Sequential Time / Parallel Time
Speedup = 24.02 / 10.13
Speedup ≈ 2.37x
```

### Performance Analysis

The **theoretical maximum speedup** for three worker threads is **3x**. The observed speedup was approximately **2.37x**. This deviation from ideal linear scaling is due to:

- **Synchronization overhead** from thread coordination
- **Lock contention** at the grill (critical section)
- **Thread management overhead**
- **Pipeline imbalance** — cooking stage takes longer than other stages, becoming the dominant bottleneck

Because cooking has the longest processing time, overall throughput is limited by the slowest stage.

---

## Conclusion

The benchmark confirms that the original bottleneck — single-worker sequential execution — was successfully reduced using **task parallelism**. Although shared resource constraints limit ideal scalability, the parallel implementation provides **substantial performance improvement** (~2.37x speedup) and demonstrates effective application of concurrency principles in a real-world scenario.
