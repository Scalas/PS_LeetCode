import pytest
from solutions.sol_2141 import Solution

cases = [
    {
        "input": {"n": 2, "batteries": [3, 3, 3]},
        "output": 4,
    },
    {
        "input": {"n": 2, "batteries": [1, 1, 1, 1]},
        "output": 2,
    },
    {
        "input": {"n": 3, "batteries": [10, 10, 3, 5]},
        "output": 8,
    },
]


@pytest.mark.sol_2141
def test_run():
    for case in cases:
        assert (
            Solution.max_run_time(
                n=case["input"]["n"],
                batteries=case["input"]["batteries"],
            )
            == case["output"]
        )
