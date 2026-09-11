# Requirements and Test Oracles

## Functional Requirements
1. The system shall identify where the most time is spent in a python script during execution. 
2. The system shall profile the performance of a suit of pytest unit tests. 
3. The system shall ...
4. The system shall ...

## Non-Functional Requirements
1. The system shall record the call stack every 1ms during execution. 
2. The system shall ...

## Test Oracles

| Requirement ID            | Requirement Description                                                   | Test Oracle (Expected Behavior)               |
|---------------------------|-----------------------------------                                        |-----------------------------------------------|
| FR-2                      | The system shall profile the performance of a suit of pytest unit tests.  | After updating the unit tests for a python program, pyinstrument can be run from the command line to profile the performance of the updated unit tests in an HTML file.  |
| NFR-1                     | The system shal record the call stack every 1ms during execution.         | When profiling a pytest suite that runs for 200ms, the pyinstrument system will record 200 records of the call stack. | 
| NFR-1                     | The system shall………...            | When…………..within 1 second.                    |
| FR-4                      | ……..                              |............                                   |
