
# Lab 10 — SonarCloud Findings

## Project Information
Project: sqe-gradebook-management
Branch: main
Tool: SonarCloud

## Initial Analysis
- Security Issues: 4
- Security Rating: C
- Duplications: 39.4%
- Quality Gate: Not computed

## Issues Identified

### Issue 1: githubactions:S8541
File: .github/workflows/ci.yml
Severity: Medium
Problem: Python packages were installed without
restricting installation to binary distributions.
Fix: Added --only-binary=:all:.

### Issue 2: githubactions:S8544
File: .github/workflows/ci.yml
Severity: Medium
Problem: Dependencies were installed without
locking their exact versions.
Fix: Created requirements.lock containing pinned
versions and verification hashes.

## Final Analysis
- Quality Gate: Passed
- Security Rating: A
- Open Issues: 0
- Duplications: 39.3%
- Coverage: No data reported

## Conclusion
SonarCloud helped identify security risks in
the GitHub Actions CI workflow. These issues
were addressed by using binary packages and
locking dependency versions. After applying
the fixes, the Quality Gate passed.
