import pytest
from solutions.sol_1497 import Solution


cases = [
    {
        "input": {"arr": [1, 2, 3, 4, 5, 10, 6, 7, 8, 9], "k": 5},
        "output": True,
    },
    {
        "input": {"arr": [1, 2, 3, 4, 5, 6], "k": 7},
        "output": True,
    },
    {
        "input": {"arr": [1, 2, 3, 4, 5, 6], "k": 10},
        "output": False,
    },
]


@pytest.mark.sol1497
def test_run():
    for case in cases:
        assert (
            Solution.can_arrange(
                arr=case["input"]["arr"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
