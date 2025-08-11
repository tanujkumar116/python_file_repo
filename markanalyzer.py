def analyze_marks(marks):
    avg = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    grade = "A" if avg >= 90 else "B" if avg >= 75 else "C" if avg >= 60 else "D"
    return avg, highest, lowest, grade

if __name__ == "__main__":
    students = {
        "Alice": [88, 92, 95, 85],
        "Bob": [72, 70, 68, 75],
        "Charlie": [95, 100, 98, 99]
    }
    for name, marks in students.items():
        avg, high, low, grade = analyze_marks(marks)
        print(f"{name} → Avg: {avg:.2f}, High: {high}, Low: {low}, Grade: {grade}")
