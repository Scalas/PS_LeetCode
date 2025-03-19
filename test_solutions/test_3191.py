import pytest
from solutions.sol_3191 import Solution


cases = [
    {
        "input": {
            "nums": [0, 1, 1, 1, 0, 0]
        },
        "output": 3,
    },
    {
        "input": {
            "nums": [0, 1, 1, 1]
        },
        "output": -1,
    },
]


@pytest.mark.sol3191
def test_run():
    for case in cases:
        assert (
            Solution.min_operations(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
