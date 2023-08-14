import pytest
from solutions.sol_1519 import Solution

cases = [
    {
        "input": {
            "n": 7,
            "edges": [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            "labels": "abaedcd",
        },
        "output": [2, 1, 1, 1, 1, 1, 1],
    },
    {
        "input": {"n": 4, "edges": [[0, 1], [1, 2], [0, 3]], "labels": "bbbb"},
        "output": [4, 2, 1, 1],
    },
    {
        "input": {"n": 5, "edges": [[0, 1], [0, 2], [1, 3], [0, 4]], "labels": "aabab"},
        "output": [3, 2, 1, 1, 1],
    },
]


@pytest.mark.sol1519
def test_run():
    for case in cases:
        assert (
            Solution.count_sub_trees(
                n=case["input"]["n"],
                edges=case["input"]["edges"],
                labels=case["input"]["labels"],
            )
            == case["output"]
        )
