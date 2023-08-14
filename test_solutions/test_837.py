import pytest
from solutions.sol_837 import Solution


cases = [
    {
        "input": {
            "n": 10,
            "k": 1,
            "max_pts": 10,
        },
        "output": 1.00000,
    },
    {
        "input": {
            "n": 6,
            "k": 1,
            "max_pts": 10,
        },
        "output": 0.60000,
    },
    {
        "input": {
            "n": 21,
            "k": 17,
            "max_pts": 10,
        },
        "output": 0.73278,
    },
    {
        "input": {
            "n": 3,
            "k": 2,
            "max_pts": 3,
        },
        "output": 0.88889,
    },
    {
        "input": {
            "n": 0,
            "k": 0,
            "max_pts": 10,
        },
        "output": 1.00000,
    },
]


@pytest.mark.sol_837
def test_run():
    for case in cases:
        assert (
            Solution.new_21_game(
                n=case["input"]["n"],
                k=case["input"]["k"],
                max_pts=case["input"]["max_pts"],
            )
            == case["output"]
        )
