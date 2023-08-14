import pytest
from solutions.sol_1579 import Solution

cases = [
    {
        "input": {
            "n": 4,
            "edges": [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]],
        },
        "output": 2,
    },
    {
        "input": {
            "n": 4,
            "edges": [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]],
        },
        "output": 0,
    },
    {
        "input": {
            "n": 4,
            "edges": [[3, 2, 3], [1, 1, 2], [2, 3, 4]],
        },
        "output": -1,
    },
    {
        "input": {
            "n": 2,
            "edges": [[1, 1, 2], [2, 1, 2], [3, 1, 2]],
        },
        "output": 2,
    },
]


@pytest.mark.sol1579
def test_run():
    for case in cases:
        assert (
            Solution.max_num_edges_to_remove(
                n=case["input"]["n"],
                edges=case["input"]["edges"],
            )
            == case["output"]
        )
