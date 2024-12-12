import pytest
from solutions.sol_2558 import Solution


cases = [
    {
        "input": {"gifts": [25, 64, 9, 4, 100], "k": 4},
        "output": 29,
    },
    {
        "input": {"gifts": [1, 1, 1, 1], "k": 4},
        "output": 4,
    },
]


@pytest.mark.sol2558
def test_run():
    for case in cases:
        assert (
            Solution.pick_gifts(
                k=case["input"]["k"],
                gifts=case["input"]["gifts"],
            )
            == case["output"]
        )
