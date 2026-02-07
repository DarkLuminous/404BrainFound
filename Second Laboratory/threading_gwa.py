import threading
import time

def compute_gwa_thread(subject_no, grade):
    print(f"[Thread-{subject_no}] Started")
    time.sleep(0.3)  # simulate processing
    print(f"[Thread-{subject_no}] Grade: {grade}")

def main():
    grades = []
    threads = []

    n = int(input("Enter number of subjects: "))

    for i in range(n):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)

    start_time = time.time()

    for i, grade in enumerate(grades):
        t = threading.Thread(
            target=compute_gwa_thread,
            args=(i + 1, grade)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    gwa = sum(grades) / len(grades)
    end_time = time.time()

    print("\n[Multithreading] Final GWA:", round(gwa, 2))
    print("[Multithreading] Execution Time:", round(end_time - start_time, 4), "seconds")

if __name__ == "__main__":
    main()