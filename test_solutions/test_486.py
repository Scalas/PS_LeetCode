import pytest
from solutions.sol_486 import Solution

cases = [
    {
        "input": {
            "nums": [1, 5, 2],
        },
        "output": False,
    },
    {
        "input": {
            "nums": [1, 5, 233, 7],
        },
        "output": True,
    },
]


@pytest.mark.sol_486
def test_run():
    for case in cases:
        assert Solution.predict_the_winner(nums=case["input"]["nums"]) == case["output"]
