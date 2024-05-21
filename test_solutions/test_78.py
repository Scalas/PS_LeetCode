import pytest
from solutions.sol_78 import Solution

cases = [
    {
        "input": {
            "nums": [1, 2, 3],
        },
        "output": [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
    },
    {
        "input": {
            "nums": [0],
        },
        "output": [[], [0]],
    },
]


@pytest.mark.sol78
def test_run():
    for case in cases:
        assert sorted(
            Solution.subsets(
                nums=case["input"]["nums"],
            )
        ) == sorted(case["output"])
