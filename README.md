# Grade Calculator

A simple Python project for calculating student grade averages and checking whether a student has passed.

## 1. Project Description

This project provides functions to:

- Calculate the average of a list of grades.
- Determine whether a student has passed (average greater than or equal to 10).
- - Grade classification into categories (upcoming feature, currently under development in PR #6).

## 2. Requirements

- Python 3.11 or later
- pip
- Git

## 3. Installation

Clone the repository:

```bash
git clone https://github.com/aminemlk2406-beep/grade-calculator.git
```

Enter the project directory:

```bash
cd grade-calculator
```

Install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## 4. Usage

Example of calculating an average:

```python
from calculator import calculate_average, is_passing

grades = [10, 12, 14]
average = calculate_average(grades)

print("Average:", average)
print("Passing:", is_passing(average))
```

Expected output:

```text
Average: 12.0
Passing: True
```

## 5. Running Tests

Run the unit tests using pytest:

```bash
python3 -m pytest -v
```

Check code style using Flake8:

```bash
python3 -m flake8 .
```

## 6. Continuous Integration

The project uses GitHub Actions to automatically run:

- Python dependency installation.
- Flake8 code style checks.
- Pytest unit tests.

The CI workflow runs on pushes and pull requests targeting the `main` branch.

## 7. Team Collaboration

The project follows a collaborative GitHub workflow:

1. Create a GitHub Issue.
2. Create a dedicated Git branch.
3. Implement and test the changes.
4. Commit and push the branch.
5. Open a Pull Request.
6. Run automated CI checks.
7. Review and merge the Pull Request.

## 8. Contributors

- Student A: Repository setup, CI configuration, documentation and reviews.
- Student B: Grade category functionality and unit tests.
- Student C: Passing-grade boundary testing and bug correction.