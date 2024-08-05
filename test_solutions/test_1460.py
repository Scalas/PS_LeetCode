import pytest
from solutions.sol_1460 import Solution


cases = [
    {
        "input": {"target": [1, 2, 3, 4], "arr": [2, 4, 1, 3]},
        "output": True,
    },
    {
        "input": {"target": [7], "arr": [7]},
        "output": True,
    },
    {
        "input": {"target": [3, 7, 9], "arr": [3, 7, 11]},
        "output": False,
    },
]


@pytest.mark.sol1460
def test_run():
    for case in cases:
        assert (
            Solution.can_be_equal(
                target=case["input"]["target"],
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
