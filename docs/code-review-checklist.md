# GradeBook code review checklist

## Correctness

- [ ] Confirm the lowest and highest distinct averages reach 0 and 100.
- [ ] Define tie, singleton, empty-roster, and missing-student behavior.

## Tests

- [ ] Assert exact ranks for a small roster with known averages.
- [ ] Cover ties, a singleton, an empty roster, and a missing student.

## Readability

- [ ] Document inputs, return values, and exceptions.
- [ ] Use names that identify the comparison and student count.

## Design

- [ ] Reuse Student.average() and GradeBook roster storage.
- [ ] Keep percentile calculation independent of roster ordering and mutation.

## Risk

- [ ] Use unique roll numbers for identity and preserve existing APIs.
- [ ] Avoid unnecessary sorting and repeated averaging.
