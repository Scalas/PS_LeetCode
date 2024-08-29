import pytest
from solutions.sol_947 import Solution

cases = [
    {
        "input": {"stones": [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]},
        "output": 5,
    },
    {
        "input": {"stones": [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]},
        "output": 3,
    },
    {
        "input": {"stones": [[0, 0]]},
        "output": 0,
    },
    {
        "input": {
            "stones": [
                [5, 9],
                [9, 0],
                [0, 0],
                [7, 0],
                [4, 3],
                [8, 5],
                [5, 8],
                [1, 1],
                [0, 6],
                [7, 5],
                [1, 6],
                [1, 9],
                [9, 4],
                [2, 8],
                [1, 3],
                [4, 2],
                [2, 5],
                [4, 1],
                [0, 2],
                [6, 5],
            ]
        },
        "output": 19,
    },
]


@pytest.mark.sol947
def test_run():
    for case in cases:
        assert (
            Solution.remove_stones(
                stones=case["input"]["stones"],
            )
            == case["output"]
        )
