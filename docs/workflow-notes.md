# SQE Workflow Notes

## Lab 2 - Task 3: Merge Conflict

The merge conflict occurred because two feature branches modified the same line in
`src/book.py` differently.

The two branches were:

- `feature/rename-field-a`
- `feature/rename-field-b`

The branches made conflicting changes to the same field. When the second branch was
merged into `main`, Git could not automatically decide which change should be kept.

The conflict was resolved locally by checking out the feature branch, merging `main`,
editing the conflict markers in `src/book.py`, keeping the correct implementation,
staging the resolved file, committing the resolution, and pushing the branch.

The conflict was then verified through GitHub and the pull request was merged after
the required checks passed.

## Lab 2 - Task 4: Commit Hygiene Audit

### Last 10 commits

Only 8 commits currently exist in the repository, so the complete available history
from `git log --oneline -10` is:

```text
d7843fb refactor(book): rename title field to student id (#5)
e979c38 docs: document conflict resolution
ac959fd refactor(book): rename title field to id number (#6)
89a5314 fix(book): correct field indentation
255969b feat(book): add Book management (#4)
ab050dc docs: add project README
9565470 chore: setup project structure and CI
8bdc557 Initial commit