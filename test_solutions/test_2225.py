import pytest
from solutions.sol_2225 import Solution

cases = [
    {
        "input": {
            "matches": [
                [1, 3],
                [2, 3],
                [3, 6],
                [5, 6],
                [5, 7],
                [4, 5],
                [4, 8],
                [4, 9],
                [10, 4],
                [10, 9],
            ],
        },
        "output": [[1, 2, 10], [4, 5, 7, 8]],
    },
    {
        "input": {
            "matches": [[2, 3], [1, 3], [5, 4], [6, 4]],
        },
        "output": [[1, 2, 5, 6], []],
    },
]


@pytest.mark.sol_2225
def test_run():
    for case in cases:
        assert (
            Solution.find_winners(
                matches=case["input"]["matches"],
            )
            == case["output"]
        )
