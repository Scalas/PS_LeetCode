import pytest
from solutions.sol_1282 import Solution

cases = [
    {
        "input": {
            "group_sizes": [3, 3, 3, 3, 3, 1, 3],
        },
        "output": [[5], [0, 1, 2], [3, 4, 6]],
    },
    {
        "input": {
            "group_sizes": [2, 1, 3, 3, 3, 2],
        },
        "output": [[1], [0, 5], [2, 3, 4]],
    },
]


@pytest.mark.sol1282
def test_run():
    for case in cases:
        assert sorted(
            Solution.group_the_people(
                group_sizes=case["input"]["group_sizes"],
            )
        ) == sorted(case["output"])
