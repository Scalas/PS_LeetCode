import pytest
from solutions.sol_1337 import Solution

cases = [
    {
        "input": {
            "mat": [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ],
            "k": 3,
        },
        "output": [2, 0, 3],
    },
    {
        "input": {
            "mat": [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]],
            "k": 2,
        },
        "output": [0, 2],
    },
]


@pytest.mark.sol1337
def test_run():
    for case in cases:
        assert (
            Solution.k_weakest_rows(
                mat=case["input"]["mat"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
