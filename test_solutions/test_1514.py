import pytest
from solutions.sol_1514 import Solution

cases = [
    {
        "input": {
            "n": 3,
            "edges": [[0, 1], [1, 2], [0, 2]],
            "succ_prob": [0.5, 0.5, 0.2],
            "start": 0,
            "end": 2,
        },
        "output": 0.25000,
    },
    {
        "input": {
            "n": 3,
            "edges": [[0, 1], [1, 2], [0, 2]],
            "succ_prob": [0.5, 0.5, 0.3],
            "start": 0,
            "end": 2,
        },
        "output": 0.30000,
    },
    {
        "input": {
            "n": 3,
            "edges": [[0, 1]],
            "succ_prob": [0.5],
            "start": 0,
            "end": 2,
        },
        "output": 0.00000,
    },
]


@pytest.mark.sol1514
def test_run():
    for case in cases:
        assert (
            Solution.max_probability(
                n=case["input"]["n"],
                edges=case["input"]["edges"],
                succ_prob=case["input"]["succ_prob"],
                start=case["input"]["start"],
                end=case["input"]["end"],
            )
            == case["output"]
        )
