import pytest
from solutions.sol_1590 import Solution


cases = [
    {
        "input": {"nums": [3, 1, 4, 2], "p": 6},
        "output": 1,
    },
    {
        "input": {"nums": [6, 3, 5, 2], "p": 9},
        "output": 2,
    },
    {
        "input": {"nums": [1, 2, 3], "p": 3},
        "output": 0,
    },
]


@pytest.mark.sol1590
def test_run():
    for case in cases:
        assert (
            Solution.min_subarray(
                p=case["input"]["p"],
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
