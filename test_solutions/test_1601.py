import pytest
from solutions.sol_1601 import Solution

cases = [
    {
        "input": {
            "n": 5,
            "requests": [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]],
        },
        "output": 5,
    },
    {
        "input": {
            "n": 3,
            "requests": [[0, 0], [1, 2], [2, 1]],
        },
        "output": 3,
    },
    {
        "input": {
            "n": 4,
            "requests": [[0, 3], [3, 1], [1, 2], [2, 0]],
        },
        "output": 4,
    },
    {
        "input": {
            "n": 3,
            "requests": [[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]],
        },
        "output": 4,
    },
    {
        "input": {
            "n": 2,
            "requests": [
                [1, 1],
                [1, 0],
                [0, 1],
                [0, 0],
                [0, 0],
                [0, 1],
                [0, 1],
                [1, 0],
                [1, 0],
                [1, 1],
                [0, 0],
                [1, 0],
            ],
        },
        "output": 11,
    },
    {
        "input": {
            "n": 3,
            "requests": [
                [1, 2],
                [2, 2],
                [0, 0],
                [1, 1],
                [0, 2],
                [0, 0],
                [2, 1],
                [0, 1],
                [1, 0],
                [2, 2],
                [0, 1],
                [2, 0],
                [2, 2],
            ],
        },
        "output": 12,
    },
    {
        "input": {
            "n": 3,
            "requests": [
                [1, 2],
                [0, 0],
                [0, 2],
                [0, 1],
                [0, 0],
                [0, 2],
                [1, 0],
                [0, 1],
                [2, 0],
            ],
        },
        "output": 7,
    },
]


@pytest.mark.sol1601
def test_run():
    for case in cases:
        assert (
            Solution.maximum_requests(
                n=case["input"]["n"],
                requests=case["input"]["requests"],
            )
            == case["output"]
        )
