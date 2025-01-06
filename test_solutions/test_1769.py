import pytest
from solutions.sol_1769 import Solution


cases = [
    {
        "input": {"boxes": "110"},
        "output": [1, 1, 3],
    },
    {
        "input": {"boxes": "001011"},
        "output": [11, 8, 5, 4, 3, 4],
    },
]


@pytest.mark.sol1769
def test_run():
    for case in cases:
        assert (
            Solution.min_operations(
                boxes=case["input"]["boxes"],
            )
            == case["output"]
        )
