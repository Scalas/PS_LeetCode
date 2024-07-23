import pytest
from solutions.sol_1636 import Solution


cases = [
    {
        "input": {"nums": [1, 1, 2, 2, 2, 3]},
        "output": [3, 1, 1, 2, 2, 2],
    },
    {
        "input": {"nums": [2, 3, 1, 3, 2]},
        "output": [1, 3, 3, 2, 2],
    },
    {
        "input": {"nums": [-1, 1, -6, 4, 5, -6, 1, 4, 1]},
        "output": [5, -1, 4, 4, -6, -6, 1, 1, 1],
    },
]


@pytest.mark.sol1636
def test_run():
    for case in cases:
        assert (
            Solution.frequency_sort(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
