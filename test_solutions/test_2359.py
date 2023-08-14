import pytest
from solutions.sol_2359 import Solution

cases = [
    {
        "input": {
            "edges": [2, 2, 3, -1],
            "node1": 0,
            "node2": 1,
        },
        "output": 2,
    },
    {
        "input": {
            "edges": [1, 2, -1],
            "node1": 0,
            "node2": 2,
        },
        "output": 2,
    },
]


@pytest.mark.sol_2359
def test_run():
    for case in cases:
        assert (
            Solution.closest_meeting_node(
                edges=case["input"]["edges"],
                node1=case["input"]["node1"],
                node2=case["input"]["node2"],
            )
            == case["output"]
        )
