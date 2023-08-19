import pytest
from solutions.sol_239 import Solution

cases = [
    {
        "input": {
            "nums": [1, 3, -1, -3, 5, 3, 6, 7],
            "k": 3,
        },
        "output": [3, 3, 5, 5, 6, 7],
    },
    {
        "input": {
            "nums": [1],
            "k": 1,
        },
        "output": [1],
    },
]


@pytest.mark.sol239
def test_run():
    for case in cases:
        assert (
            Solution.max_sliding_window(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
