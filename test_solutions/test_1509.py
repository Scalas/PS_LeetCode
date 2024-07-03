import pytest
from solutions.sol_1509 import Solution


cases = [
    {
        "input": {"nums": [5, 3, 2, 4]},
        "output": 0,
    },
    {
        "input": {"nums": [1, 5, 0, 10, 14]},
        "output": 1,
    },
    {
        "input": {"nums": [3, 100, 20]},
        "output": 0,
    },
]


@pytest.mark.sol1509
def test_run():
    for case in cases:
        assert (
            Solution.min_difference(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
