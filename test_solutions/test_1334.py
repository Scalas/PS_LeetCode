import pytest
from solutions.sol_1334 import Solution


cases = [
    {
        "input": {
            "n": 4,
            "edges": [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]],
            "distanceThreshold": 4,
        },
        "output": 3,
    },
    {
        "input": {
            "n": 5,
            "edges": [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
            "distanceThreshold": 2,
        },
        "output": 0,
    },
]


@pytest.mark.sol1334
def test_run():
    for case in cases:
        assert (
            Solution.find_the_city(
                n=case["input"]["n"],
                edges=case["input"]["edges"],
                distanceThreshold=case["input"]["distanceThreshold"],
            )
            == case["output"]
        )
