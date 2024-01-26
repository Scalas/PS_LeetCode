import pytest
from solutions.sol_576 import Solution

cases = [
    {
        "input": {"m": 2, "n": 2, "max_move": 2, "start_row": 0, "start_column": 0},
        "output": 6,
    },
    {
        "input": {"m": 1, "n": 3, "max_move": 3, "start_row": 0, "start_column": 1},
        "output": 12,
    },
]


@pytest.mark.sol_576
def test_run():
    for case in cases:
        assert (
            Solution.find_paths(
                m=case["input"]["m"],
                n=case["input"]["n"],
                max_move=case["input"]["max_move"],
                start_row=case["input"]["start_row"],
                start_column=case["input"]["start_column"],
            )
            == case["output"]
        )
