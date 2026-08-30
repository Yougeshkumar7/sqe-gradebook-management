# Workflow Notes

## Merge Conflict Resolution

A merge conflict occurred in `src/book.py` when merging
`feature/rename-field-b` with `main`.

The conflict happened because both branches changed the same
part of the `Book` class.

The conflict was resolved locally by keeping the required
`student_id` field and the validation for empty and whitespace-only
book titles and authors.

After resolving the conflict, the changes were committed and
pushed to GitHub. The pull request was then reviewed and merged
into `main`.