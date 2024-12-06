import pytest
from solutions.sol_2554 import Solution


cases = [
    {
        "input": {"banned": [1, 6, 5], "n": 5, "max_sum": 6},
        "output": 2,
    },
    {
        "input": {"banned": [1, 2, 3, 4, 5, 6, 7], "n": 8, "max_sum": 1},
        "output": 0,
    },
    {
        "input": {"banned": [11], "n": 7, "max_sum": 50},
        "output": 7,
    },
]


@pytest.mark.sol2554
def test_run():
    for case in cases:
        assert (
            Solution.max_count(
                n=case["input"]["n"],
                banned=case["input"]["banned"],
                max_sum=case["input"]["max_sum"],
            )
            == case["output"]
        )
