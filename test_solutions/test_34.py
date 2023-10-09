import pytest

from solutions.sol_34 import Solution

cases = [
    {
        "input": {"nums": [5, 7, 7, 8, 8, 10], "target": 8},
        "output": [3, 4],
    },
    {
        "input": {"nums": [5, 7, 7, 8, 8, 10], "target": 6},
        "output": [-1, -1],
    },
    {
        "input": {"nums": [], "target": 0},
        "output": [-1, -1],
    },
]


@pytest.mark.sol34
def test_run():
    for case in cases:
        assert (
            Solution.search_range(
                nums=case["input"]["nums"],
                target=case["input"]["target"],
            )
            == case["output"]
        )
