import pytest
from solutions.sol_2192 import Solution


cases = [
    {
        "input": {
            "n": 8,
            "edges": [
                [0, 3],
                [0, 4],
                [1, 3],
                [2, 4],
                [2, 7],
                [3, 5],
                [3, 6],
                [3, 7],
                [4, 6],
            ],
        },
        "output": [
            [],
            [],
            [],
            [0, 1],
            [0, 2],
            [0, 1, 3],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3],
        ],
    },
    {
        "input": {
            "n": 5,
            "edges": [
                [0, 1],
                [0, 2],
                [0, 3],
                [0, 4],
                [1, 2],
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
                [3, 4],
            ],
        },
        "output": [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]],
    },
]


@pytest.mark.sol2192
def test_run():
    for case in cases:
        assert (
            Solution.get_ancestors(
                n=case["input"]["n"],
                edges=case["input"]["edges"],
            )
            == case["output"]
        )
