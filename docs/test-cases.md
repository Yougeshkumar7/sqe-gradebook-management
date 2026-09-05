# GradeBook Test Cases

| ID | Title | Requirement | Preconditions | Steps | Expected | Priority | Type | Result | Execution Note |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | Add valid score | REQ-1 | Student exists | Create student; add score 85. | Score 85 is added. | High | Positive | Pass | Score 85 was successfully added. |
| TC-002 | Reject negative score | REQ-2 | Student exists | Create student; add score -5. | ValueError is raised; scores remain empty. | High | Negative | Pass | Negative score was correctly rejected. |
| TC-003 | Reject non-numeric score | REQ-3 | Student exists | Create student; add score "abc". | TypeError is raised; scores remain empty. | High | Negative | Pass | Non-numeric score was correctly rejected. |
| TC-004 | Calculate average | REQ-4 | Student has scores | Add 80; add 90; calculate average. | Average is 85.0. | High | Functional | Pass | Average was correctly calculated as 85.0. |
| TC-005 | Average with no scores | REQ-4 | Student has no scores | Calculate average. | Returns 0.0. | Medium | Boundary | Pass | Empty score list correctly returned 0.0. |
| TC-006 | Average with one score | REQ-4 | Student has no scores | Add 75; calculate average. | Returns 75.0. | Medium | Functional | Pass | Single score correctly returned 75.0. |
| TC-007 | Reject duplicate roll number | REQ-5 | GradeBook contains roll number 101 | Create another student with 101; add student. | ValueError is raised; student is not added. | High | Negative | Pass | Duplicate roll number was correctly rejected. |
| TC-008 | Case-insensitive name search | REQ-6 | Student "Ali" exists | Search for "ali". | Correct student is found. | Medium | Functional | Pass | Student was found using different letter case. |
| TC-009 | Maximum score boundary | REQ-7 | Student exists | Add score 100. | Score 100 is accepted. | High | Boundary | Pass | Maximum score of 100 was accepted. |
| TC-010 | Minimum score boundary | REQ-7 | Student exists | Add score 0. | Score 0 is accepted. | High | Boundary | Pass | Minimum score of 0 was accepted. |
| TC-011 | Mid-range grade conversion | REQ-8 | Student exists | Convert score 75 to grade. | Returns "B". | Medium | Functional | Pass | Score 75 was correctly converted to grade B. |
| TC-012 | Grade conversion boundary | REQ-8 | Student exists | Convert score 80 to grade. | Returns "A". | High | Boundary | Pass | Score 80 was correctly converted to grade A. |