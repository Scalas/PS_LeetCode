import pytest
from solutions.sol_3396 import Solution


cases = [
    {
        "input": {"nums": [1, 2, 3, 4, 2, 3, 3, 5, 7]},
        "output": 2,
    },
    {
        "input": {"nums": [4, 5, 6, 4, 4]},
        "output": 2,
    },
    {
        "input": {"nums": [6, 7, 8, 9]},
        "output": 0,
    },
]


@pytest.mark.sol3396
def test_run():
    for case in cases:
        assert (
            Solution.minimum_operations(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
