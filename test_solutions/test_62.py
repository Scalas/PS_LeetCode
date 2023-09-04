import pytest
from solutions.sol_62 import Solution

cases = [
    {
        "input": {"n": 7, "m": 3},
        "output": 28,
    },
    {
        "input": {"n": 3, "m": 7},
        "output": 28,
    },
    {
        "input": {"n": 2, "m": 3},
        "output": 3,
    },
]


@pytest.mark.sol62
def test_run():
    for case in cases:
        assert (
            Solution.unique_paths(
                n=case["input"]["n"],
                m=case["input"]["m"],
            )
            == case["output"]
        )
