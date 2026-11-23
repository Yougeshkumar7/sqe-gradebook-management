# GradeBook code review checklist

## Correctness

- [x] Confirm the lowest and highest distinct averages reach 0 and 100.
- [x] Define tie, singleton, empty-roster, and missing-student behavior.

## Tests

- [x] Assert exact ranks for a small roster with known averages.
- [x] Cover ties, a singleton, an empty roster, and a missing student.

## Readability

- [x] Document inputs, return values, and exceptions.
- [x] Use names that identify the comparison and student count.

## Design

- [x] Reuse Student.average() and GradeBook roster storage.
- [x] Keep percentile calculation independent of roster ordering and mutation.

## Risk

- [x] Use unique roll numbers for identity and preserve existing APIs.
- [x] Avoid unnecessary sorting and repeated averaging.

## Lessons learned

Checking both endpoints caught the most valuable defect. Dividing by the
roster size produced 50 for the top student in a two-student roster, while
the original lowest-rank test still passed. Dividing by the number of peers
restores the 0 and 100 endpoints for distinct averages.

Next time, check that a detached object with the same identifier uses the
stored record's data. The regression test demonstrates this with stale scores.
