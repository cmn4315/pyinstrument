## Project Overview
Pyinstrument is a profiler for python code that allows developers to measure the execution time of portions of python
code, with the goal of locating performance bottlenecks. This allows developers to more easily optimize their code by
drawing attention to the least optimized (read: slowest) sections. Pyinstrument's developers also focus on efficiency,
minimizing performance overhead caused by the profiler in order to improve accuracy. Over the course of the semester,
this project aims to apply the various testing techniques discussed in SWEN-777 to the pyinstrument repository, in order
to measure and evaluate the extent to which the project meets key quality standards that we identify based on existing
documentation. Those metrics are listed in the following section.

## Key Quality Metrics

- Accuracy; How close are pyinstrument's results to actual execution times?
    - Measured by net and percent difference between pyinstrument's results and the results of another profiler and
    between pyinstrument results on easily comparable pieces of code.

- Efficiency; How close does the project get to maintianing minimal overhead while profiling code?
    - Measured by difference in program execution time when using versus not using the profiler.

- Maintainability; How easily can the project be updated/maintained by open-source contributors?
    - Code Structure; How well-structured is the source code for the project?
        - Measured by Lines of Code (LOC) per module/file, comment density, and possibly cyclomatic/cognitive complexity.
    - Testability; How easily can the project be tested, and how thoroughly is the project currently tested?
        - Measured by number of unit test cases per test suite and by test coverage (line coverage, branch coverage,
        etc.)

