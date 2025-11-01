

students = [
    {"name": "Alice", "scores": [90, 88, 95]},
    {"name": "Brian", "scores": [70, 75, 68]},
    {"name": "Cynthia", "scores": [85, 80, 82]},
    {"name": "David", "scores": [50, 60, 55]},
    {"name": "Ella", "scores": [92, 95, 98]},
]


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 45:
        return "D"
    else:
        return "F"

def calculate_averages(students):
    for s in students:
        avg = sum(s["scores"]) / len(s["scores"])
        s["average"] = round(avg, 2)
        s["grade"] = assign_grade(avg)
    return students

def sort_scoresheet(students):
    return sorted(students, key=lambda x: x["average"], reverse=True)

def get_class_average(students):
    total = sum(s["average"] for s in students)
    return round(total / len(students), 2)

def get_top_student(students):
    return max(students, key=lambda x: x["average"])

def print_report(students):
    print("=" * 40)
    print("CLASS REPORT".center(40))
    print("=" * 40)

    class_avg = get_class_average(students)
    top = get_top_student(students)

    print(f"Class Average : {class_avg}")
    print(f"Top Student   : {top['name']} - {top['average']}")
    print("\nScoresheet (Ordered by Average):\n")

    print(f"{'Name':<10} | {'Average':<7} | {'Grade'}")
    print("-" * 30)
    for s in students:
        print(f"{s['name']:<10} | {s['average']:<7} | {s['grade']}")
    print("=" * 40)


students = calculate_averages(students)
sorted_students = sort_scoresheet(students)
print_report(sorted_students)
