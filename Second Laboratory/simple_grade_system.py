"""
Simple Grade Computing System - Beginner-Friendly Version
Demonstrates basic multithreading and multiprocessing
"""

import threading
import time
from multiprocessing import Process

# ============================================================================
# MULTITHREADING VERSION
# ============================================================================

def compute_gwa_thread(subject, grade):
    """Calculate GWA for one subject using threading"""
    print(f"[Thread] Processing {subject}: {grade}")
    # Simulate some processing time
    time.sleep(0.1)
    print(f"[Thread] Completed {subject}")

def run_threading_version(grades_dict):
    """Run the multithreading version"""
    print("\n=== MULTITHREADING ===")
    start_time = time.time()
    
    threads = []
    
    # Create a thread for each subject
    for subject, grade in grades_dict.items():
        t = threading.Thread(target=compute_gwa_thread, args=(subject, grade))
        threads.append(t)
        t.start()
    
    # Wait for all threads to finish
    for t in threads:
        t.join()
    
    # Calculate overall GWA
    gwa = sum(grades_dict.values()) / len(grades_dict)
    
    end_time = time.time()
    print(f"\nOverall GWA: {gwa:.2f}")
    print(f"Time taken: {end_time - start_time:.4f} seconds\n")
    
    return gwa, end_time - start_time


# ============================================================================
# MULTIPROCESSING VERSION
# ============================================================================

def compute_gwa_process(subject, grade):
    """Calculate GWA for one subject using multiprocessing"""
    print(f"[Process] Processing {subject}: {grade}")
    # Simulate some processing time
    time.sleep(0.1)
    print(f"[Process] Completed {subject}")

def run_multiprocessing_version(grades_dict):
    """Run the multiprocessing version"""
    print("\n=== MULTIPROCESSING ===")
    start_time = time.time()
    
    processes = []
    
    # Create a process for each subject
    for subject, grade in grades_dict.items():
        p = Process(target=compute_gwa_process, args=(subject, grade))
        processes.append(p)
        p.start()
    
    # Wait for all processes to finish
    for p in processes:
        p.join()
    
    # Calculate overall GWA
    gwa = sum(grades_dict.values()) / len(grades_dict)
    
    end_time = time.time()
    print(f"\nOverall GWA: {gwa:.2f}")
    print(f"Time taken: {end_time - start_time:.4f} seconds\n")
    
    return gwa, end_time - start_time


# ============================================================================
# USER INPUT
# ============================================================================

def get_grades_from_user():
    """Get grades from user input"""
    grades = {}
    
    num_subjects = int(input("How many subjects? "))
    
    for i in range(num_subjects):
        subject = input(f"\nSubject {i+1} name: ")
        grade = float(input(f"Grade for {subject}: "))
        grades[subject] = grade
    
    return grades


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    print("="*50)
    print("GRADE COMPUTING SYSTEM")
    print("="*50)
    
    # Option to use sample data or user input
    use_sample = input("\nUse sample data? (y/n): ").lower()
    
    if use_sample == 'y':
        grades = {
            "Mathematics": 85,
            "Science": 90,
            "English": 78,
            "History": 92
        }
        print("\nUsing sample grades:")
        for subject, grade in grades.items():
            print(f"  {subject}: {grade}")
    else:
        grades = get_grades_from_user()
    
    # Run both versions
    thread_gwa, thread_time = run_threading_version(grades)
    process_gwa, process_time = run_multiprocessing_version(grades)
    
    # Compare results
    print("="*50)
    print("COMPARISON")
    print("="*50)
    print(f"{'Method':<20} {'Time (seconds)':<15}")
    print("-"*50)
    print(f"{'Threading':<20} {thread_time:<15.4f}")
    print(f"{'Multiprocessing':<20} {process_time:<15.4f}")
    print("="*50)


if __name__ == "__main__":
    main()