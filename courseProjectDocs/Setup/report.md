# Test Suite Summary

The primary tests for Pyinstrument is a suite of Python unit tests (using the pytest framework) to directly test the backend functionality of the tool. Built into the unit tests are some tests to cover the command line interface of this tool, which acts as the main frontend through which users are able to run Pyinstrument.

# Baseline Coverage Metrics

## Test Statistics

- Tests Run: 132
- Tests Skipped: 11
- Tests Passed: 132
- Tests Failed: 0 (1 warning)

## Coverage Summary

- Statement Coverage: Out of 2398 total statements idenfitified by pyest-cov, all but 718 statements are covered by the existing unit test suite. This amounts to a total statement coverage of 70% across the entire Pyinstrument project.

- Branch Coverage: From the 770 total branches found by pytest-cov, there are 128 branches that were only partially covered by the unit test suite.

- Total Coverage: Combining statement coverage and branch coverage, as (statements executed + branches executed) / (total statements + total branches), the overall test coverage of this project is currently 67% according to pytest-cov.

## Observations

Since this project is primarily a command line tool to profile python scripts during development, there is no real UI to test and therefore there is no suite of UI tests.

The C code from the low_level folder of Pyinstrument does not seem to be directly tested (through unit tests or otherwise). However, the low_level code seems to be primarily sourced from another project, and is indirectly tested through testing of the remainder of the project (since the "high level" code depends on these low_level files).
