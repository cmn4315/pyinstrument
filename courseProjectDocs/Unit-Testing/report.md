# New Test Cases & Rationale

## test_statprofile.py:

- test_profiler_requires_timer_function(): tests a previously untested branch of an if-else statement, which checks whether a timer function was provided when required. The test ensures that the correct TypeError is raised when no timer function is provided.
- test_profiler_rejects_invalid_timer(): tests a previously untested branch of an if-else statement, which checks that the provided timer_type is one of the expected valid options. This test ensures that the correct ValueError is raised when a timer_type outside the expected options is provided.
- test_profiler_uses_timer_function(): tests a previously untested branch of the profiler constructor, which sets the profile's timer function to the provided function, if the specified timer_type is timer_func. This test ensures that the profile is properly constructed with the provided timer_func.
- test_profiler_profile_calls_target(): tests one path through the profile() method, which was previously completely untested. This test verifies that the provided dummy callback function is called by the profile method.
- test_profiler_walltime_thread_subscribes(): tests a previously untested branch of an if-else statement, which handles when the specified timer_type is walltime_thread. This test ensures that the timing thread is correctly subscribed to, with the specified interval and correct subscription ID.

# New Test Results

- Tests Run: 137
- Tests Skipped: 11
- Tests Passed: 137
- Tests Failed: 0 (1 warning)

# Coverage Improvement Analysis

The additional tests for stat_profile_python.py increased this file's statement coverage from 72% to 85%, by covering an additional 10 statements. This additional coverage was achieved by using the pytest-cov html report to identify untested statements, then writing 5 new tests to address 4 untested branches and 1 path of a previously untested method. Improving the coverage of this individual file also raised the total test coverage of pyinstrument from 70% to 71%.

The previously untested branches in stat_profile_python.py were likely skipped because they are not commonly used, or were easy to manually validate the functionality of. However, the fact that the profile() method was untested was a bit surprising, since this seems to be a core method of stat_profile_python. There was mention in the documentation that some low level files were pulled from another source, so it's possible the developers are trusting these files to work as intended, and only feel the need to test features that they add or change.
