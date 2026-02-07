from multiprocessing import Process
import time
import os

def compute_gwa_process(subject_no, grade):
    print(f"[Process-{subject_no} | PID {os.getpid()}] Grade: {grade}")
    time.sleep(0.3)  # simulate processing

def main():
    grades = []
    processes = []

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)

    start_time = time.time()

    for i, grade in enumerate(grades):
        p = Process(
            target=compute_gwa_process,
            args=(i + 1, grade)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    gwa = sum(grades) / len(grades)
    end_time = time.time()

    print("\n[Multiprocessing] Final GWA:", round(gwa, 2))
    print("[Multiprocessing] Execution Time:", round(end_time - start_time, 4), "seconds")

if __name__ == "__main__":
    main()