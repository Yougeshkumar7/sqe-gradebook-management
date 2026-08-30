# Triage Meeting Log

## Priority Ranking

1. Issue #8 — average() crashes when student has no scores
   - Severity: High
   - Priority: P1
   - Reason: A crash directly prevents grade statistics from being calculated.

2. Issue #10 — duplicate roll numbers are allowed
   - Severity: High
   - Priority: P1
   - Reason: Duplicate identifiers can corrupt student and grade records.

3. Issue #9 — student ID accepts an empty value
   - Severity: Medium
   - Priority: P2
   - Reason: Invalid student records can be created, but the system does not immediately crash.

4. Issue #11 — negative scores are accepted
   - Severity: Medium
   - Priority: P2
   - Reason: Invalid grades can affect statistics, but the issue is less urgent than the P1 defects.

5. Issue #12 — average() gives incorrect rounding
   - Severity: Low
   - Priority: P3
   - Reason: The system continues working and the impact is limited to incorrect rounding.

## Severity and Priority Trade-offs

Issue #9 has Medium severity and P2 priority because invalid IDs affect data quality but do not immediately crash the system.

Issue #12 has Low severity and P3 priority because incorrect rounding has limited impact and can safely be deferred while higher-impact defects are fixed.

## Deferred This Sprint

Issues #11 and #12 will not be fixed this sprint because they have lower immediate impact than the P1 defects and can be addressed in a later sprint.
