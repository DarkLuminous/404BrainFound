"""
Grade Computing System - Multithreading vs Multiprocessing
A comprehensive grade calculator demonstrating concurrent execution
"""

import threading
import time
from multiprocessing import Process, Queue
import statistics

# ============================================================================
# MULTITHREADING IMPLEMENTATION
# ============================================================================

class ThreadGradeCalculator:
    def __init__(self):
        self.results = []
        self.lock = threading.Lock()
    
    def compute_gwa(self, subject_name, grade, thread_id):
        """Calculate GWA for a single subject using threading"""
        time.sleep(0.01)  # Simulate processing time
        gwa = grade  # Individual grade contribution
        
        # Thread-safe result storage
        with self.lock:
            self.results.append((subject_name, gwa, thread_id))
            print(f"[Thread-{thread_id}] {subject_name}: {grade} - Processed")
    
    def calculate_overall_gwa(self, subjects_grades):
        """Calculate GWA using multithreading"""
        print("\n" + "="*60)
        print("MULTITHREADING APPROACH")
        print("="*60)
        
        self.results = []
        threads = []
        
        start_time = time.time()
        
        # Create and start threads for each subject
        for idx, (subject, grade) in enumerate(subjects_grades.items(), 1):
            t = threading.Thread(
                target=self.compute_gwa, 
                args=(subject, grade, idx)
            )
            threads.append(t)
            t.start()
        
        # Wait for all threads to complete
        for t in threads:
            t.join()
        
        # Calculate final GWA
        if self.results:
            grades = [grade for _, grade, _ in self.results]
            final_gwa = statistics.mean(grades)
        else:
            final_gwa = 0
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"\n[RESULT] Overall GWA: {final_gwa:.2f}")
        print(f"[TIME] Execution Time: {execution_time:.6f} seconds")
        
        return final_gwa, execution_time, self.results


# ============================================================================
# MULTIPROCESSING IMPLEMENTATION
# ============================================================================

def compute_gwa_process(subject_name, grade, process_id, queue):
    """Calculate GWA for a single subject using multiprocessing"""
    time.sleep(0.01)  # Simulate processing time
    gwa = grade
    result = (subject_name, gwa, process_id)
    queue.put(result)
    print(f"[Process-{process_id}] {subject_name}: {grade} - Processed")


class ProcessGradeCalculator:
    def calculate_overall_gwa(self, subjects_grades):
        """Calculate GWA using multiprocessing"""
        print("\n" + "="*60)
        print("MULTIPROCESSING APPROACH")
        print("="*60)
        
        processes = []
        queue = Queue()
        
        start_time = time.time()
        
        # Create and start processes for each subject
        for idx, (subject, grade) in enumerate(subjects_grades.items(), 1):
            p = Process(
                target=compute_gwa_process, 
                args=(subject, grade, idx, queue)
            )
            processes.append(p)
            p.start()
        
        # Wait for all processes to complete
        for p in processes:
            p.join()
        
        # Collect results from queue
        results = []
        while not queue.empty():
            results.append(queue.get())
        
        # Calculate final GWA
        if results:
            grades = [grade for _, grade, _ in results]
            final_gwa = statistics.mean(grades)
        else:
            final_gwa = 0
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"\n[RESULT] Overall GWA: {final_gwa:.2f}")
        print(f"[TIME] Execution Time: {execution_time:.6f} seconds")
        
        return final_gwa, execution_time, results


# ============================================================================
# USER INPUT AND MAIN EXECUTION
# ============================================================================

def get_user_grades():
    """Get grades from user input with validation"""
    print("\n" + "="*60)
    print("GRADE COMPUTING SYSTEM")
    print("="*60)
    
    subjects_grades = {}
    
    # Get number of subjects
    while True:
        try:
            num_subjects = int(input("\nHow many subjects? "))
            if num_subjects > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get subject names and grades
    for i in range(num_subjects):
        subject = input(f"\nSubject {i+1} name: ").strip()
        
        while True:
            try:
                grade = float(input(f"Grade for {subject} (0-100): "))
                if 0 <= grade <= 100:
                    subjects_grades[subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    return subjects_grades


def generate_large_dataset(n=1000):
    """Generate a large dataset for performance testing"""
    import random
    subjects_grades = {}
    for i in range(n):
        subjects_grades[f"Subject_{i+1}"] = random.uniform(70, 100)
    return subjects_grades


def compare_methods(subjects_grades):
    """Compare multithreading and multiprocessing methods"""
    print("\n" + "="*60)
    print("COMPARING BOTH METHODS")
    print("="*60)
    
    # Multithreading
    thread_calc = ThreadGradeCalculator()
    thread_gwa, thread_time, thread_results = thread_calc.calculate_overall_gwa(subjects_grades)
    
    # Multiprocessing
    process_calc = ProcessGradeCalculator()
    process_gwa, process_time, process_results = process_calc.calculate_overall_gwa(subjects_grades)
    
    # Display comparison table
    print("\n" + "="*60)
    print("COMPARISON TABLE")
    print("="*60)
    print(f"{'Method':<20} {'GWA':<15} {'Execution Time (s)':<20}")
    print("-" * 60)
    print(f"{'Multithreading':<20} {thread_gwa:<15.2f} {thread_time:<20.6f}")
    print(f"{'Multiprocessing':<20} {process_gwa:<15.2f} {process_time:<20.6f}")
    print("=" * 60)
    
    # Execution order comparison
    print("\n" + "="*60)
    print("EXECUTION ORDER ANALYSIS")
    print("="*60)
    print("\nMultithreading order:")
    for subject, grade, thread_id in sorted(thread_results, key=lambda x: x[2]):
        print(f"  Thread-{thread_id}: {subject}")
    
    print("\nMultiprocessing order:")
    for subject, grade, process_id in sorted(process_results, key=lambda x: x[2]):
        print(f"  Process-{process_id}: {subject}")


def main():
    """Main execution function"""
    print("Welcome to the Grade Computing System!")
    print("\nChoose an option:")
    print("1. Enter grades manually")
    print("2. Test with large dataset (1000 subjects)")
    
    choice = input("\nYour choice (1 or 2): ").strip()
    
    if choice == "1":
        subjects_grades = get_user_grades()
    elif choice == "2":
        print("\nGenerating 1000 random grades...")
        subjects_grades = generate_large_dataset(1000)
        print("Dataset generated!")
    else:
        print("Invalid choice. Using default dataset.")
        subjects_grades = {
            "Mathematics": 85,
            "Science": 90,
            "English": 78,
            "History": 92,
            "Computer Science": 88
        }
    
    # Compare both methods
    compare_methods(subjects_grades)


if __name__ == "__main__":
    main()