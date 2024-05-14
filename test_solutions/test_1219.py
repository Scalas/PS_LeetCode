import pytest
from solutions.sol_1219 import Solution

cases = [
    {
        "input": {
            "grid": [[0, 6, 0], [5, 8, 7], [0, 9, 0]],
        },
        "output": 24,
    },
    {
        "input": {
            "grid": [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]],
        },
        "output": 28,
    },
    {
        "input": {
            "grid": [
                [0, 0, 0, 0, 0, 0, 32, 0, 0, 20],
                [0, 0, 2, 0, 0, 0, 0, 40, 0, 32],
                [13, 20, 36, 0, 0, 0, 20, 0, 0, 0],
                [0, 31, 27, 0, 19, 0, 0, 25, 18, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 18, 0, 6],
                [0, 0, 0, 25, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 21, 0, 30, 0, 0, 0, 0],
                [19, 10, 0, 0, 34, 0, 2, 0, 0, 27],
                [0, 0, 0, 0, 0, 34, 0, 0, 0, 0],
            ],
        },
        "output": 129,
    },
]


@pytest.mark.sol1218
def test_run():
    for case in cases:
        assert (
            Solution.get_maximum_gold(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
