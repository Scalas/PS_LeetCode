import pytest
from solutions.sol_1420 import Solution

cases = [
    {
        "input": {
            "n": 2,
            "m": 3,
            "k": 1,
        },
        "output": 6,
    },
    {
        "input": {
            "n": 5,
            "m": 2,
            "k": 3,
        },
        "output": 0,
    },
    {
        "input": {
            "n": 9,
            "m": 1,
            "k": 1,
        },
        "output": 1,
    },
    {
        "input": {
            "n": 50,
            "m": 100,
            "k": 25,
        },
        "output": 34549172,
    },
]


@pytest.mark.sol1420
def test_run():
    for case in cases:
        assert (
            Solution.num_of_arrays(
                n=case["input"]["n"], m=case["input"]["m"], k=case["input"]["k"]
            )
            == case["output"]
        )
