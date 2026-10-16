# Unit Testing Notes — Lab 7

## 1. Objective

To develop and document unit testing practices for the Gradebook Management System using pytest.

## 2. Arrange–Act–Assert (AAA)

- **Arrange:** Prepare the required test data.
- **Act:** Execute the function being tested.
- **Assert:** Verify that the actual result matches the expected result.

## 3. Pytest Fixtures

Fixtures provide reusable test data and reduce repeated setup code.

- **Function scope:** Creates a new fixture for every test function.
- **Module scope:** Creates a fixture once per test module and shares it across tests.

Function scope is suitable for independent tests. Module scope is useful for expensive setup that can safely be shared.

## 4. Gradebook Test Cases

The test suite should cover:

- Adding students.
- Adding scores.
- Validating scores.
- Calculating student averages.
- Handling empty inputs and boundary cases.
- Testing invalid inputs where applicable.

## 5. Mocking File Operations

Mocking replaces a real dependency with a simulated object during testing.

Mocking the built-in `open()` function allows file-writing behavior to be tested without creating an actual file. File-operation failures should also be tested to verify error handling.

## 6. Parametrized Testing

The `@pytest.mark.parametrize` decorator allows multiple input cases to be tested using one test function.

Examples include valid scores, boundary values, negative scores, and scores above the allowed maximum. Descriptive test IDs make failures easier to identify.

## 7. Running Tests

Run these commands from the repository root.

### Verbose Output

```bash
pytest -v lab7/tests/
```

Verbose mode displays individual test names and their results.

**Screenshot:** Add your actual terminal screenshot here.

### Short Traceback Output

```bash
pytest --tb=short
```

Short traceback mode displays a compact error report when a test fails.

**Screenshot:** Add your actual terminal screenshot here.

## 8. Pytest Configuration

The `pytest.ini` file can contain:

```ini
[pytest]
testpaths = lab7/tests
python_files = test_*.py
```

This configuration specifies the test directory and filename pattern. Adjust `testpaths` if your project uses a different test directory.

## 9. Conclusion

Unit testing improves the reliability and maintainability of the Gradebook Management System. Fixtures reduce duplication, mocking isolates dependencies, and parametrized tests simplify edge-case testing. Consistent pytest configuration also