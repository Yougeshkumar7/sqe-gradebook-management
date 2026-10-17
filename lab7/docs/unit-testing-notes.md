# Unit Testing Notes — Lab 7

## Objective
The objective of this lab is to test the GradeBook program using pytest and verify that its functions work correctly.

## 1. Unit Testing
Unit testing checks individual functions or components to ensure they work as expected.

## 2. Arrange, Act, Assert (AAA)
- **Arrange:** Prepare the test data.
- **Act:** Run the function being tested.
- **Assert:** Check whether the result is correct.

## 3. Fixtures
Pytest fixtures provide reusable test data or setup.

- **Function scope:** Runs once for each test function.
- **Module scope:** Runs once per module.

## 4. Class Average Tests
Test the class average function using different scores, including normal values and edge cases.

## 5. Mocking File I/O
Mocking replaces real file operations during testing. It allows us to test saving data and handling errors without depending on actual files.

## 6. Parametrized Tests
Parametrization runs the same test with multiple input values, reducing repeated code.

## 7. Running Tests
Run all Lab 7 tests:

```bash
python -m pytest -v lab7/tests/
```

Run tests with shorter error reports:

```bash
python -m pytest --tb=short
```

## Conclusion
Pytest fixtures, assertions, mocking, and parametrization help make unit tests reusable, organized, and reliable.
