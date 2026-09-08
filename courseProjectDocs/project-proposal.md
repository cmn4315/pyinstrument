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
            - LoC per file: 85
            - Comment density: 0.062 (6.2% of lines are comments)
    - Testability; How easily can the project be tested, and how thoroughly is the project currently tested?
        - Measured by number of unit test cases per test suite and by test coverage (line coverage, branch coverage,
        etc.)
        - Total tests: 77
        - Tests per file: 5.92
        - Test Classes: 1
        - Tests per class: 18
        - Coverage: 78%


### Testability Metric Results
#### testability-metrics.py output
```
Searching for test files...
	Test file found: test_ipython_magic.py
		Number of test classes: 0
		Total number of tests: 7

	Test file found: test_processors.py
		Number of test classes: 0
		Total number of tests: 8

	Test file found: test_threading.py
		Number of test classes: 0
		Total number of tests: 1

	Test file found: test_overflow.py
		Number of test classes: 0
		Total number of tests: 5

	Test file found: test_stack_sampler.py
		Number of test classes: 0
		Total number of tests: 7

	Test file found: test_cmdline.py
		Number of test classes: 1
		Total number of tests: 18
		Average tests per suite in file: 18.0

	Test file found: test_django_middleware.py
		Number of test classes: 0
		Total number of tests: 2

	Test file found: test_context_manager.py
		Number of test classes: 0
		Total number of tests: 2

	Test file found: test_profiler_async.py
		Number of test classes: 0
		Total number of tests: 4

	Test file found: test_profiler.py
		Number of test classes: 0
		Total number of tests: 12

	Test file found: test_cmdline_main.py
		Number of test classes: 0
		Total number of tests: 3

	Test file found: test_pstats_renderer.py
		Number of test classes: 0
		Total number of tests: 3

	Test file found: test_renderers.py
		Number of test classes: 0
		Total number of tests: 5


Found 77 tests and 1 test suites in 13 total test files.
	Average tests per suite: 18.0
	Average tests per file: 5.923076923076923
	Average suites per file: 0.07692307692307693
```

#### Coverage
```
Name                                                 Stmts   Miss  Cover
------------------------------------------------------------------------
noxfile.py                                              36     36     0%
pyinstrument/__init__.py                                 9      2    78%
pyinstrument/__main__.py                               273    114    58%
pyinstrument/context_manager.py                         56      1    98%
pyinstrument/frame.py                                  216     17    92%
pyinstrument/frame_info.py                              16      0   100%
pyinstrument/frame_ops.py                               73      9    88%
pyinstrument/low_level/pyi_timing_thread_python.py      54     38    30%
pyinstrument/low_level/stat_profile_python.py           75     21    72%
pyinstrument/low_level/types.py                          2      0   100%
pyinstrument/magic/__init__.py                           1      1     0%
pyinstrument/magic/_utils.py                            37     37     0%
pyinstrument/magic/magic.py                            132    132     0%
pyinstrument/middleware.py                              71     45    37%
pyinstrument/processors.py                             119     13    89%
pyinstrument/profiler.py                               125     19    85%
pyinstrument/renderers/__init__.py                       8      0   100%
pyinstrument/renderers/base.py                          46      3    93%
pyinstrument/renderers/console.py                      179      5    97%
pyinstrument/renderers/html.py                          74     15    80%
pyinstrument/renderers/jsonrenderer.py                  47      1    98%
pyinstrument/renderers/pstatsrenderer.py                53      0   100%
pyinstrument/renderers/session.py                       10      3    70%
pyinstrument/renderers/speedscope.py                    87      2    98%
pyinstrument/session.py                                 93     14    85%
pyinstrument/stack_sampler.py                          178     40    78%
pyinstrument/typing.py                                  12      1    92%
pyinstrument/util.py                                    69     26    62%
pyinstrument/vendor/__init__.py                          0      0   100%
pyinstrument/vendor/decorator.py                       259    148    43%
pyinstrument/vendor/keypath.py                          24     13    46%
setup.py                                                 6      6     0%
test/__init__.py                                         0      0   100%
test/conftest.py                                        27      1    96%
test/fake_time_util.py                                  52      0   100%
test/low_level/__init__.py                               0      0   100%
test/low_level/test_context.py                          50      2    96%
test/low_level/test_custom_timer.py                     39      1    97%
test/low_level/test_floatclock.py                       22      0   100%
test/low_level/test_frame_info.py                       67      2    97%
test/low_level/test_setstatprofile.py                   37      1    97%
test/low_level/test_threaded.py                         33      2    94%
test/low_level/test_timing_thread.py                    65      2    97%
test/low_level/util.py                                   6      0   100%
test/test_cmdline.py                                   150      2    99%
test/test_cmdline_main.py                               40      0   100%
test/test_context_manager.py                            24      0   100%
test/test_django_middleware.py                          31      0   100%
test/test_ipython_magic.py                             116     87    25%
test/test_overflow.py                                   36      0   100%
test/test_processors.py                                128      0   100%
test/test_profiler.py                                  212      1    99%
test/test_profiler_async.py                            143      1    99%
test/test_pstats_renderer.py                            75      0   100%
test/test_renderers.py                                  58      0   100%
test/test_stack_sampler.py                             104      1    99%
test/test_threading.py                                  28      0   100%
test/util.py                                            53     11    79%
------------------------------------------------------------------------
TOTAL                                                 4036    876    78%
================================================================================ 136 passed, 7 skipped, 5561 warnings in 13.70s ================================================================================
```
