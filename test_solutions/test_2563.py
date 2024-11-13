import pytest
from solutions.sol_2563 import Solution


cases = [
    {
        "input": {
            "nums": [0, 1, 7, 4, 4, 5], "lower": 3, "upper": 6
        },
        "output": 6,
    },
    {
        "input": {
            "nums": [1, 7, 9, 2, 5], "lower": 11, "upper": 11
        },
        "output": 1,
    },
]


@pytest.mark.sol2563
def test_run():
    for case in cases:
        assert (
            Solution.countFairPairs(
                nums=case["input"]["nums"],
                lower=case["input"]["lower"],
                upper=case["input"]["upper"],
            )
            == case["output"]
        )
