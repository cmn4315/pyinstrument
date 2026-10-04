# New Test Cases & Rationale

## Unit Testing I
### test_statprofile.py:

- test_profiler_requires_timer_function(): tests a previously untested branch of an if-else statement, which checks whether a timer function was provided when required. The test ensures that the correct TypeError is raised when no timer function is provided.
- test_profiler_rejects_invalid_timer(): tests a previously untested branch of an if-else statement, which checks that the provided timer_type is one of the expected valid options. This test ensures that the correct ValueError is raised when a timer_type outside the expected options is provided.
- test_profiler_uses_timer_function(): tests a previously untested branch of the profiler constructor, which sets the profile's timer function to the provided function, if the specified timer_type is timer_func. This test ensures that the profile is properly constructed with the provided timer_func.
- test_profiler_profile_calls_target(): tests one path through the profile() method, which was previously completely untested. This test verifies that the provided dummy callback function is called by the profile method.
- test_profiler_walltime_thread_subscribes(): tests a previously untested branch of an if-else statement, which handles when the specified timer_type is walltime_thread. This test ensures that the timing thread is correctly subscribed to, with the specified interval and correct subscription ID.

### test_renderers.py:

- test_session_renderer_renders_json(): tests a previously untested class, SessionRenderer. This is a class which
renders a pyinstrument session as json, which seems to have been somewhat unused prior and therefore not tested.
- test_console_renderer_flat_xor_timeline(): tests a configuration parameter constraint in the ConsoleRenderer class.
Specifically, ConsoleRenderer does not support both the `flat` and `timeline` arguments being True at the same time.
- test_console_renderer_percent_of_total_time(): tests a previously untested branch within the rendering logic of
ConsoleRenderer, specifically the mode in which time is shown as a percentage of total time.
- test_html_renderer_options_deprecated(): tests that providing deprecated options within the HTMLRenderer constructor test_profiler_uses_timer_function the
proper warnings, which were previously untested.
- test_html_renderer_open_in_browser(): tests the previously untested `open_in_browser()` method within HTMLRenderer,
which opens the rendered HTML in the browser.

## Unit Testing II
### test_middleware.py:

- test_process_request_started_profiler(): directly tests the process_request() method of the ProfilerMiddleware class in middleware.py with a stubbed Profiler class. This validates that the profiler is properly created and started in response to a request.
- test_process_response_renders_html(): directly tests the major branch in the process_response() method of the ProfilerMiddleware class in middleware.py with stubbed Profiler, Renderer, and HTMLRenderer classes. This validates that a request is properly processed and a response is provided back to the requester.

### test_stack_sampler.py:

- test_uses_coarse_timer_when_resolution_is_sufficient(): Mocks the C language utilities that the stack sampler uses to
check machine timer resolution in order to directly test the timer type chosen by the stack sampler when the machine-
specific timer resolution is sufficiently accurate to use the coarse timer.
- test_uses_walltimer_when_resolution_above_interval(): Mocks the same C utilities as the above case, instead testing
the other branch of the timer choice conditional.
- test_timer_func_used_when_use_timing_thread_false(): Mocks the stack sampler's `setstackprofile()` method in order to
verify that it is correctly called with arguments to configure use of a provided timer function, rather than the
default timer thread, when the stack sampler is started with `use_timer_thread = False`
- test_timer_thread_used_correctly(): Again mocks `setstackprofile()` to verify the inverse of the above test: that
`setstackprofile()` is called with the arguments to use the timer thread when `use_timer_thread = True`.
- test_rollback_on_C_hooks_failure_during_subscribe(): Mocks an exception in the C language utilities to test the stack
sampler's rollback logic performs correctly when such a failure happens

# New Test Results

- Tests Run: 153
- Tests Skipped: 7
- Tests Passed: 153
- Tests Failed: 0 (1 warning)

# Coverage Improvement Analysis (Unit Testing I)

The additional tests for stat_profile_python.py increased this file's statement coverage from 72% to 85%, by covering an additional 10 statements. This additional coverage was achieved by using the pytest-cov html report to identify untested statements, then writing 5 new tests to address 4 untested branches and 1 path of a previously untested method. Improving the coverage of this individual file also raised the total test coverage of pyinstrument from 70% to 71%.

The previously untested branches in stat_profile_python.py were likely skipped because they are not commonly used, or were easy to manually validate the functionality of. However, the fact that the profile() method was untested was a bit surprising, since this seems to be a core method of stat_profile_python. There was mention in the documentation that some low level files were pulled from another source, so it's possible the developers are trusting these files to work as intended, and only feel the need to test features that they add or change.

The tests added to test_renderers.py increased the coverage of three files, `renderers/session.py`, `renderers/console.py` and `renderers/html.py`. `console.py` coverage was increased from 97% to 98% with 2 newly covered statements, `session.py` coverage was increased from 70% to 100% with 3 newly covered statements, and `html.py` coverage was increased from 80% to 96% with 12 newly covered statements. `pyinstrument/session.py` also gained 1 additional statement of coverage, though this was unintentional. In total, 18 new statements were covered by the added tests.

The previously untested statements covered by these new tests fall into 3 broad categories. First, the lines in the SessionRenderer class were previously untested likely due to the relative lack of use that this class sees within the codebase. The class is also very small, and the functionality is very easy to manually verify. Second, there are the constructor lines checking for configuration parameter validity, again likely untested due to the ease of manual verification, a dedicated test could be deemed unnecessary to validate the functionality. Nevertheless, it is important that even those easily verifiable statements be tested, as it removed the need for that manual verification to be performed. Improved coverage and more comprehensive tests are never a bad thing. Finally, the final category of newly covered statements are actual, functional lines that were simple omitted in the existing tests. This is the category into which the html renderer's `open_in_browser()` method and the ConsoleRenderer's percent_of_total time option fall. These lines were uncovered while representing significant pieces of functionality. Adding these tests further verifies the correctness of these classes.

# Coverage Improvement Analysis (Unit Testing II)

The additional tests for middleware.py were primarily intended to increase the overall coverage of the class. This additional coverage was achieved by testing some previously untested branches in the ProfilerMiddleware class, by stubbing out the Profile classes used by this middleware component. Largely, before these new tests, middleware was tested indirectly through test runs of the Profiler components, so the tactic of stubbing these Profilers helped us test the ProfilerMiddleware more directly. In total, these tests brought the statement coverage of middleware.py from 38% to 61%, and improved the total statement coverage of the entire codebase from 71% to 72%. The middleware component is a part of the core functionality of pyinstrument, so increasing its statement coverage is definitely valuable, and it's surprising that coverage started out as low as it did.

The tests added for `stack_sampler.py` were added mostly for the purpose of utilizing mocking to bypass machine-specific
information that affected test coverage. By mocking the low-level C code used by the stack sampler, we were able to
control the values that would normally be influenced by the hardware platform on which the program was running, thereby
allowing us to test the sampler configuration logic that depends on those low level values. While the coverage of
stack_sampler.py was only increased from 78% to 80% and only 4 new lines were covered by these tests, they represent a
better approach to testing low level code. Rather than allowing the tests to use real machine-specific values, we mock
those values in order to enable testing of the logic itself without depending on low level utilities and the real timer
resolution values. We also made use of exception mocking to simulate a failure in those low-level C utilities, allowing
testing of the rollback logic's execution in that event.
