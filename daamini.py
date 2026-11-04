import time
import random
import matplotlib.pyplot as plt

# ==================================================
# STUDENT DATABASE (list of dictionaries)
# ==================================================
students = [
    {"roll": 101, "name": "Aarav",  "course": "MCA", "marks": 82},
    {"roll": 102, "name": "Simran", "course": "MCA", "marks": 91},
    {"roll": 103, "name": "Rohan",  "course": "MCA", "marks": 76},
    {"roll": 104, "name": "Simran", "course": "BCA", "marks": 68},
    {"roll": 105, "name": "Kabir",  "course": "MCA", "marks": 88},
]

# ==================================================
# 1. LINEAR SEARCH
# ==================================================
def linear_search(records, field, value):
    comparisons = 0
    matches = []
    for index, rec in enumerate(records):
        comparisons += 1                      # one record checked
        stored = rec[field]
        if isinstance(stored, str):
            found = stored.lower() == str(value).lower()
        else:
            found = stored == value
        if found:
            matches.append(index)
            if field == "roll":               # roll number is unique
                break
    return matches, comparisons

# ==================================================
# 2. ADD / DISPLAY
# ==================================================
def print_record(rec):
    print(f"Roll: {rec['roll']} | Name: {rec['name']} | "
          f"Course: {rec['course']} | Marks: {rec['marks']}")

def add_student():
    try:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ").strip()
        course = input("Enter course: ").strip()
        marks = float(input("Enter marks (0-100): "))
    except ValueError:
        print("Invalid input. Roll must be an integer and marks a number.")
        return
    if roll <= 0 or not name or not course:
        print("Roll must be positive; name and course cannot be empty.")
        return
    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return
    matches, _ = linear_search(students, "roll", roll)
    if matches:
        print("A student with this roll number already exists.")
        return
    students.append({"roll": roll, "name": name,
                     "course": course, "marks": marks})
    print("Student added successfully.")

def display_all():
    if not students:
        print("No records available.")
        return
    print(f"\nTotal records: {len(students)}")
    for rec in students:
        print_record(rec)

# ==================================================
# 3. SEARCH OPERATIONS
# ==================================================
def search_by_roll():
    try:
        roll = int(input("Enter roll number to search: "))
    except ValueError:
        print("Roll number must be an integer.")
        return
    start = time.perf_counter()
    matches, comparisons = linear_search(students, "roll", roll)
    elapsed = time.perf_counter() - start
    if matches:
        print("\nRecord found at position", matches[0] + 1)
        print_record(students[matches[0]])
    else:
        print("\nRecord not found.")
    print("Comparisons made:", comparisons)
    print(f"Execution Time: {elapsed:.6f} seconds")

def search_by_name():
    name = input("Enter name to search: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    start = time.perf_counter()
    matches, comparisons = linear_search(students, "name", name)
    elapsed = time.perf_counter() - start
    if matches:
        print(f"\n{len(matches)} record(s) found:")
        for i in matches:
            print_record(students[i])
    else:
        print("\nRecord not found.")
    print("Comparisons made:", comparisons)
    print(f"Execution Time: {elapsed:.6f} seconds")

# ==================================================
# 4. PERFORMANCE ANALYSIS (worst case)
# ==================================================
def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]
    times = []
    for n in sizes:
        data = [{"roll": i, "name": "Student" + str(i),
                 "course": "MCA", "marks": random.randint(0, 100)}
                for i in range(1, n + 1)]
        total = 0
        for _ in range(5):                    # average of 5 runs
            start = time.perf_counter()
            linear_search(data, "roll", n + 1)   # not present -> n comparisons
            total += time.perf_counter() - start
        avg = total / 5
        times.append(avg)
        print(f"Size: {n} | Comparisons: {n} | Avg Time: {avg:.6f} sec")

    plt.plot(sizes, times, marker='o')
    plt.title("Linear Search Performance (Worst Case)")
    plt.xlabel("Number of Records (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.show()

# ==================================================
# MAIN MENU
# ==================================================
def main():
    while True:
        print("\n====== STUDENT RECORD SEARCH (LINEAR SEARCH) ======")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search by Roll Number")
        print("4. Search by Name")
        print("5. Performance Analysis")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all()
        elif choice == "3":
            search_by_roll()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            performance_analysis()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()  
