def calculate_average(grades):
    if not grades:
        raise ValueError("Grades list cannot be empty")
    return sum(grades) / len(grades)


def is_passing(average):
    return average >= 10


def get_grade_category(average):
    if average >= 16:
        return "Excellent"
    if average >= 12:
        return "Good"
    if average >= 10:
        return "Average"
    return "Fail"
