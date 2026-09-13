# Requirements and Test Oracles

## Functional Requirements
1. The system shall identify where the most time is spent in a python script during execution.
2. The system shall profile the performance of a suite of pytest unit tests.
3. The system shall profile only a particular region of Python code when invoked via the Python API.
4. The system shall show the profiling results for the portion of the program that executed when the program is exited
   early via keyboard interrupt.

## Non-Functional Requirements
1. The system shall record the call stack every 1ms during execution.
2. The system shall add minimal overhead to the runtime of a program.

## Test Oracles

| Requirement ID            | Requirement Description                                                   | Test Oracle (Expected Behavior)               |
|---------------------------|-----------------------------------                                        |-----------------------------------------------|
| FR-2                      | The system shall profile the performance of a suit of pytest unit tests.  | After updating the unit tests for a python program, pyinstrument can be run from the command line to profile the performance of the updated unit tests in an HTML file.  |
| NFR-1                     | The system shall record the call stack every 1ms during execution.         | When profiling a pytest suite that runs for 200ms, the pyinstrument system will record 200 records of the call stack. |
| FR-3                     | The system shall profile only a particular region of Python code when invoked via the Python API.| When a Python program is run which uses the pyinstrument Python API, only the correct portion of the program is profiled. |
| NFR-2                      | The system shall add minimal overhead to the runtime of a program. | When a program is
profiled, the total execution time should not exceed 150% of the program's runtime when not profiled. |
