# Maintainability Metrics

To run the code we used to measure the maintainability metrics of this project (LoC per file and comment density), simply run the maintainability_metrics.py file in this directory. This will evaluate the main pyinstrument folder (with the actual codebase, exluding rext code and documentation).
- If any errors occur, ensure that you are running the file from the root directory of this repository.

# Testability Metrics
To run the code used to measure testability metrics of this project, run `python3
courseProjectCode/Metrics/testability-metrics.py` from the root directory of this project. This will show a report on
total number of tests, test suites, and test files, along with tests per suite, suites per file, and tests per file. For
test coverage metrics, first run `pip install -r requirements-dev.txt` and `pip install pytest-cov`, then run `pytest --cov=. test/`
from the root directory of the project.

