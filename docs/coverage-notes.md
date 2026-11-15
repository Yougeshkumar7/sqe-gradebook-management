
# Lab 11 — Automated Test Coverage

## Project Information
Project: sqe-gradebook-management
Tool: pytest-cov and coverage.py
Python Version: 3.11

## Baseline Coverage
- Line Coverage: 93%
- Branch Coverage: 82%
- Overall Coverage: 88%
- Missing Statements: 4
- Partial Branches: 7

## Identified Coverage Gaps

### 1. grade_letter()
Lines 38 and 41 were uncovered.
Tests were added for invalid score types and
scores outside the valid range.

### 2. find_student_by_name()
Line 71 was uncovered.
A test was added to check that None is returned
when a student cannot be found.

### 3. find_student_by_roll_number()
Line 78 was uncovered.
A test was added for a nonexistent roll number.

### 4. add_student()
Line 61 was partially covered.
Additional tests exercised the loop with
different roll numbers.

## Final Coverage
- Line Coverage: 100%
- Branch Coverage: 100%
- Overall Coverage: 100%
- Missing Statements: 0
- Partial Branches: 0

## Coverage vs. Test Quality
Code coverage measures how much code is executed
during testing, but it does not guarantee that
the tests check the correct results.

For example, a test that only verifies that a
function runs without raising an exception may
provide coverage without verifying its output.

Stronger assertions verify expected return values,
changes in program state, and error handling.

## Conclusion
Additional tests were introduced to cover missing
statements and branches in the Gradebook project.

Overall coverage improved from 88% to 100%.
Both line and branch coverage reached 100%.
