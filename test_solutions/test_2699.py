import pytest
from solutions.sol_2699 import Solution


cases = [
    {
        "input": {
            "n": 5,
            "edges": [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]],
            "source": 0,
            "destination": 1,
            "target": 5,
        },
        "output": [[4, 1, 3], [2, 0, 6], [0, 3, 1], [4, 3, 1]],
    },
    {
        "input": {
            "n": 3,
            "edges": [[0, 1, -1], [0, 2, 5]],
            "source": 0,
            "destination": 2,
            "target": 6,
        },
        "output": [],
    },
    {
        "input": {
            "n": 4,
            "edges": [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]],
            "source": 0,
            "destination": 2,
            "target": 6,
        },
        "output": [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, 1]],
    },
    {
        "input": {
            "n": 4,
            "edges": [[3, 0, -1], [1, 2, -1], [2, 3, -1], [1, 3, 9], [2, 0, 5]],
            "source": 0,
            "destination": 1,
            "target": 7,
        },
        "output": [[3, 0, 5], [1, 2, 2], [2, 3, 8], [1, 3, 9], [2, 0, 5]],
    },
]


@pytest.mark.sol2699
def test_run():
    for case in cases:
        assert (
            Solution.modified_graph_edges(
                target=case["input"]["target"],
                n=case["input"]["n"],
                destination=case["input"]["destination"],
                edges=case["input"]["edges"],
                source=case["input"]["source"],
            )
            == case["output"]
        )
