import random
from threading import Thread
from multiprocessing import Process
import time


class GWAComparison:

    def __init__(self, grades):
        self.grades = grades

    def thread_task(self, grade):
        # Simulate I/O-bound work
        time.sleep(0.01)

    def process_task(self, grade):
        # Simulate I/O-bound work
        time.sleep(0.01)

    def run_multithreading(self):
        threads = []
        start = time.time()

        for grade in self.grades:
            t = Thread(target=self.thread_task, args=(grade,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return time.time() - start

    def run_multiprocessing(self):
        processes = []
        start = time.time()

        for grade in self.grades:
            p = Process(target=self.process_task, args=(grade,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        return time.time() - start


def display_large_dataset(grades):
    print(f"\nGenerated {len(grades)} grades")
    print("Sample grades (first 10):", grades[:10])
    print("Sample grades (last 10):", grades[-10:])
    print("Minimum grade:", min(grades))
    print("Maximum grade:", max(grades))


def main():
    print("\n=== GWA Concurrency Comparison ===")
    print("1. Manual grade input")
    print("2. Auto-generate 1000 grades")

    choice = input("Choose option: ")

    if choice == "1":
        n = int(input("Number of subjects: "))
        grades = [float(input(f"Grade {i+1}: ")) for i in range(n)]
    else:
        grades = [random.randint(75, 95) for _ in range(1000)]
        display_large_dataset(grades)

    gwa = sum(grades) / len(grades)
    print("GWA:", round(gwa, 2))

    system = GWAComparison(grades)

    t_time = system.run_multithreading()
    p_time = system.run_multiprocessing()

    print("\nExecution Time Comparison")
    print("Multithreading:", round(t_time, 4), "seconds")
    print("Multiprocessing:", round(p_time, 4), "seconds")


if __name__ == "__main__":
    main()
