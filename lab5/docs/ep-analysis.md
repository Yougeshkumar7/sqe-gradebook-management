# Equivalence Partitioning Analysis

## 1. Score / Letter Grade

For the score, we divided the possible inputs into different groups
called equivalence classes. Instead of testing every possible score,
we selected one representative score from each group.

| Equivalence Class | Range | Representative | Expected Result |
|---|---|---:|---|
| Invalid-low | Less than 0 | -10 | ValueError |
| F | 0–59 | 45 | F |
| D | 60–69 | 65 | D |
| C | 70–79 | 75 | C |
| B | 80–89 | 85 | B |
| A | 90–100 | 95 | A |
| Invalid-high | Greater than 100 | 150 | ValueError |

## 2. Number of Scores

A student should have at least 1 score and can have a maximum of 6
scores. We divided the possible number of scores into three groups.

| Equivalence Class | Range | Representative | Expected Result |
|---|---|---:|---|
| Invalid-low | 0 scores | 0 | ValueError |
| Valid | 1–6 scores | 3 | Accepted |
| Invalid-high | 7 or more scores | 8 | ValueError |

## 3. Student Name

For the student name, the name should not be empty, should not be
longer than 50 characters, and should contain only letters, spaces,
or hyphens.

| Equivalence Class | Example | Representative | Expected Result |
|---|---|---|---|
| Valid name | yougesh kumar | yougesh kumar | Accepted |
| Empty string | Empty | "" | ValueError |
| Over-length | More than 50 characters | 51 characters | ValueError |
| Contains digits | yougesh123 | yougesh123 | ValueError |
| Contains symbols | yougesh@kumar | yougesh@kumar | ValueError |

## EP Limitation

Equivalence Partitioning helps us reduce the number of test cases by
choosing one value from each group instead of testing every possible
input.

However, it may miss some errors at the boundaries of the groups.
For example, an error between 59 and 60 or between 89 and 90 might not
be found using only Equivalence Partitioning.

Boundary Value Analysis will be used in Lab 6 to test these boundary
values.

## Pytest Run Summary

The complete pytest results will be added below after running all the
Lab 5 test cases.





---

## — Check your final Lab 5 files

Your folder should now look like:

```text
lab5/
│
├── docs/
│   └── ep-analysis.md
│
├── src/
│   ├── __init__.py
│   └── gradebook.py
│
├── tests/
│   ├── test_letter_grade.py
│   ├── test_roster.py
│   └── test_validate_name.py
│
└── pytest.ini