# Unit Testing — Lab 7

## 1. Objective

To implement and document unit testing practices for the Gradebook Management System using pytest.

## 2. Arrange–Act–Assert (AAA)

- **Arrange:** Prepare the required data.
- **Act:** Execute the function.
- **Assert:** Check the expected result.

## 3. Fixtures

Fixtures provide reusable test data and reduce repeated setup code.

- **Function scope:** Creates a fresh fixture for every test function.
- **Module scope:** Creates a fixture once per test module and reuses it.

Function scope is useful for independent tests. Module scope is useful for expensive setup that can safely be shared.

## 4. Gradebook Test Cases

The test suite should cover:

- Adding students.
- Adding scores.
- Validating scores.
- Calculating student averages.
- Empty inputs and boundary cases.
- Invalid inputs where applicable.

## 5. Mocking

Mocking replaces a real dependency with a simulated object.

For file operations, mocking `open()` allows tests to verify file-writing behavior without creating an actual file. Error handling can be tested by making `open()` raise an `OSError`.

## 6. Parametrized Testing

The `@pytest.mark.parametrize` decorator tests multiple input cases using one test function.

Examples include valid scores, boundary scores, negative scores, and scores above the allowed maximum. Descriptive test IDs help identify failed cases.

## 7. Running Tests

Run these commands from the project root.

### Verbose Output

```bash
pytest -v tests/
```

Displays individual test names and their results.

**Screenshot:** Add your verbose test output here.

### Short Traceback

```bash
pytest --tb=short
```

Displays a shorter traceback when a test fails.

**Screenshot:** Add your short traceback output here.

## 8. Pytest Configuration

The `pytest.ini` file should contain:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
```

This configures test discovery.

**Screenshot:** Add a screenshot of `pytest.ini` here.

## 9. Conclusion

Unit testing improves software reliability. Fixtures reduce duplication, mocking isolates dependencies, and parametrized tests simplify edge-case testing. Consistent pytest configuration also helps prepare the project for continuous integration.