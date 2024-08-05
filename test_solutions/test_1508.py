import pytest
from solutions.sol_1508 import Solution


cases = [
    {
        "input": {"nums": [1, 2, 3, 4], "n": 4, "left": 1, "right": 5},
        "output": 13,
    },
    {
        "input": {"nums": [1, 2, 3, 4], "n": 4, "left": 3, "right": 4},
        "output": 6,
    },
    {
        "input": {"nums": [1, 2, 3, 4], "n": 4, "left": 1, "right": 10},
        "output": 50,
    },
]


@pytest.mark.sol1508
def test_run():
    for case in cases:
        assert (
            Solution.range_sum(
                n=case["input"]["n"],
                right=case["input"]["right"],
                left=case["input"]["left"],
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
