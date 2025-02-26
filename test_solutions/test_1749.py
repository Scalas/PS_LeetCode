import pytest
from solutions.sol_1749 import Solution


cases = [
    {
        "input": {"nums": [1, -3, 2, 3, -4]},
        "output": 5,
    },
    {
        "input": {"nums": [2, -5, 1, -4, 3, -2]},
        "output": 8,
    },
]


@pytest.mark.sol1749
def test_run():
    for case in cases:
        assert (
            Solution.max_absolute_sum(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
