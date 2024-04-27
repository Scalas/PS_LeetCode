import pytest
from solutions.sol_514 import Solution

cases = [
    {
        "input": {
            "ring": "godding",
            "key": "gd",
        },
        "output": 4,
    },
    {
        "input": {
            "ring": "godding",
            "key": "godding",
        },
        "output": 13,
    },
]


@pytest.mark.sol_514
def test_run():
    for case in cases:
        assert (
            Solution.find_rotate_steps(
                ring=case["input"]["ring"],
                key=case["input"]["key"],
            )
            == case["output"]
        )
