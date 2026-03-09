# Elevator Project

A program consisting of a command-line interface that simulates an elevator traveling between floors and calculates the total travelling time.

## Problem Statement

Given:

- A starting floor
- An ordered list of floors to visit

Simulate an elevator traveling between floors and output:

1. The total travel time
2. The sequence of floors visited

### Program Constant

* Time to travel one floor: `10` units

### Example

Input:

```
start=12 floors=2,9,1,32
```

Output:

```
560 12,2,9,1,32
```

Explanation:

```
12 -> 2 = 10 floors = 100 time
2 -> 9 = 7 floors = 70 time
9 -> 1 = 8 floors = 80 time
1 -> 32 = 31 floors = 310 time
-----------------------------
Total time = 560
```

### Project Structure
```
Elevator-Project/
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ main.py                  # CLI parser logic and program output
│  └─ elevator/
│     ├─ __init__.py
│     └─ simulator.py          # Elevator logic
└─ tests/
   ├─ test_main.py             # Tests for CLI parsing
   └─ test_simulator.py        # Tests for elevator simulation
```

### How to Run
Install the dependencies in requirements.txt (only pytest for running the tests)

To run the elevator, either run:
- python src/main.py --start [floor you want to start from] --floors [list of integers of consecutive floors to visit]
or
- ./src/main.py --start [floor you want to start from] --floors [list of integers of consecutive floors to visit]

To run the tests, either run:
- pytest
or
- python -m pytest

## Assumptions

1. Duplicate floors shouldn't be logged, as the elevator does no work and does not move.
2. The program inputs should be passed through the CLI arguments, as user inputs within a runnable program wouldn't be as quick to run and test.
3. The parser should allow string inputs as long as it can be reasonably converted to an integer array, as the instructions had no restrictions against data types of inputs.
4. The output should be a string, as the instructions had the example output as "560 12,2,9,1,32", and outputting the tuple itself would make it appear as "(560, [12,2,9,1,32])".
5. Negative floors should be allowed (basements), as the instructions had no restrictions against them.
---


