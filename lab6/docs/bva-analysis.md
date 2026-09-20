# Boundary Value Analysis

## 1. Score / Letter Grade

Boundary Value Analysis (BVA) tests the values immediately below,
at, and immediately above important boundaries.

The score domain is 0–100.

The letter-grade boundaries are:

- 60 → D
- 70 → C
- 80 → B
- 90 → A

The domain boundaries are:

- 0 → minimum valid score
- 100 → maximum valid score

### Boundary Table

| Boundary | Value - 1 | Boundary Value | Value + 1 | Expected Results |
|---|---:|---:|---:|---|
| 0 | -1 | 0 | 1 | -1 = ValueError, 0 = F, 1 = F |
| 60 | 59 | 60 | 61 | 59 = F, 60 = D, 61 = D |
| 70 | 69 | 70 | 71 | 69 = D, 70 = C, 71 = C |
| 80 | 79 | 80 | 81 | 79 = C, 80 = B, 81 = B |
| 90 | 89 | 90 | 91 | 89 = B, 90 = A, 91 = A |
| 100 | 99 | 100 | 101 | 99 = A, 100 = A, 101 = ValueError |

---

## 2. Roster Score-Count Rule

According to the Lab 5 requirement, a student must have between
1 and 6 scores.

Therefore:

- 0 scores → invalid
- 1–6 scores → valid
- 7 or more scores → invalid

### Boundary Values

| Boundary | Value - 1 | Boundary Value | Value + 1 | Expected Result |
|---|---:|---:|---:|---|
| 1 | 0 | 1 | 2 | 0 = Invalid, 1 = Valid, 2 = Valid |
| 6 | 5 | 6 | 7 | 5 = Valid, 6 = Valid, 7 = Invalid |

For the complete boundary-focused tests, the required values are:

0, 1, 2, 5, 6, 7.

---

## 3. Name Length

According to the Lab 5 requirement, a student name must be non-empty
and have a maximum length of 50 characters.

Therefore:

- 0 characters → invalid
- 1–50 characters → valid if the characters satisfy the name rules
- More than 50 characters → invalid

### Boundary Values

| Boundary | Value - 1 | Boundary Value | Value + 1 | Expected Result |
|---|---:|---:|---:|---|
| 1 | 0 | 1 | 2 | 0 = Invalid, 1 = Valid, 2 = Valid |
| 50 | 49 | 50 | 51 | 49 = Valid, 50 = Valid, 51 = Invalid |

For the complete boundary-focused tests, the required lengths are:

0, 1, 49, 50, 51.

---

## 4. Why Boundary Value Analysis Is Useful

Equivalence Partitioning tests representative values from each
equivalence class. However, EP can miss defects at the edges of
classes.

Boundary Value Analysis focuses specifically on these edges by
testing the value immediately below, the boundary itself, and the
value immediately above.

This helps detect off-by-one errors such as using `<` instead of
`<=`.


## 5. Test Results

The Boundary Value Analysis test suite was executed using pytest.

The final test run produced:

29 passed

All BVA tests for letter_grade(), Roster, and validate_name()
passed successfully.x