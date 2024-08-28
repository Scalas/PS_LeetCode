import pytest
from solutions.sol_1905 import Solution


cases = [
    {
        "input": {
            "grid1": [
                [1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 1, 1],
            ],
            "grid2": [
                [1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0],
            ],
        },
        "output": 3,
    },
    {
        "input": {
            "grid1": [
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1],
            ],
            "grid2": [
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1],
            ],
        },
        "output": 2,
    },
]


@pytest.mark.sol1905
def test_run():
    for case in cases:
        assert (
            Solution.count_sub_islands(
                grid1=case["input"]["grid1"],
                grid2=case["input"]["grid2"],
            )
            == case["output"]
        )
