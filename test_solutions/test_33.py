import pytest

from solutions.sol_33 import Solution

cases = [
    {
        "input": {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0},
        "output": 4,
    },
    {
        "input": {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3},
        "output": -1,
    },
    {
        "input": {"nums": [1], "target": 0},
        "output": -1,
    },
]


@pytest.mark.sol33
def test_run():
    for case in cases:
        assert (
            Solution.search(
                nums=case["input"]["nums"],
                target=case["input"]["target"],
            )
            == case["output"]
        )
