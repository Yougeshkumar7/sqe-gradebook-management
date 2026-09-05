# GradeBook Test Plan

## 1. Introduction

This Test Plan defines the testing activities for the GradeBook module. The purpose is to verify that student records, scores, averages, and grade-letter conversion work correctly. Testing will focus on functional behavior and error handling of the GradeBook Python code.

## 2. Test Items

The following GradeBook components will be tested:

- `Student` class
- `Student.add_score()`
- `Student.average()`
- `Student.grade_letter()`
- `GradeBook.add_student()`
- `GradeBook.find_student_by_name()`
- `GradeBook.find_student_by_roll_number()`

## 3. Features to be Tested

The following features will be tested:

- Adding valid scores.
- Rejecting negative and non-numeric scores.
- Calculating student averages.
- Handling empty and single-score lists.
- Rejecting duplicate roll numbers.
- Case-insensitive student name search.
- Accepting minimum and maximum scores of 0 and 100.
- Converting scores into grade letters.

## 4. Features Not to be Tested

User interface testing is out of scope because the current GradeBook is a Python library/module and does not provide a graphical user interface. Performance testing and database integration testing are also out of scope because these features are not implemented in the current codebase.

## 5. Test Approach

Testing will use functional and negative test cases. Each test case will have defined preconditions, steps, expected results, priority, and test type. Manual execution will be performed using the current GradeBook code, with results recorded as Pass, Fail, or Blocked.

## 6. Pass/Fail Criteria

The test cycle will be considered successful when at least 95% of the planned test cases pass and zero Critical defects remain open. Any failed test case must be investigated and linked to a GitHub Issue when a defect is identified.

## 7. Test Deliverables

The following test deliverables will be produced:

- `docs/test-plan.md`
- `docs/test-cases.md`
- `docs/rtm.md`
- Manual test execution results
- GitHub defect issues for any failed test cases

## 8. Environmental Needs

Testing requires Python, the GradeBook source code, and the project test environment. Tests will be executed locally using the repository's Python environment and pytest where applicable. GitHub will be used to record and track defects.

## 9. Schedule

- Test Plan preparation: Task 1
- Test Case preparation: Task 2
- Requirements Traceability Matrix: Task 3
- Manual Test Execution: Task 4
- Defect reporting and documentation: After execution

## 10. Risks

Potential risks include incorrect validation of scores, unexpected behavior at boundary values, duplicate student records, and differences between expected and actual grade-letter conversion. Changes to the GradeBook code during testing may also affect previously tested functionality.



## 11. Functional Requirements

- REQ-1: The system shall allow a student to add a valid numeric score.
- REQ-2: The system shall reject negative scores.
- REQ-3: The system shall reject non-numeric scores.
- REQ-4: The system shall calculate the average of a student's scores.
- REQ-5: The system shall reject duplicate roll numbers when adding students.
- REQ-6: The system shall find students by name without considering letter case.
- REQ-7: The system shall accept scores from the minimum value of 0 to the maximum value of 100.
- REQ-8: The system shall convert numeric scores into the corresponding grade letter.