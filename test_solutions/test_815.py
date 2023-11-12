import pytest
from solutions.sol_815 import Solution

cases = [
    {
        "input": {
            "routes": [[1, 2, 7], [3, 6, 7]],
            "source": 1,
            "target": 6,
        },
        "output": 2,
    },
    {
        "input": {
            "routes": [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]],
            "source": 15,
            "target": 12,
        },
        "output": -1,
    },
    {
        "input": {
            "routes": [[1, 7], [3, 5]],
            "source": 5,
            "target": 5,
        },
        "output": 0,
    },
]


@pytest.mark.sol_815
def test_run():
    for case in cases:
        assert (
            Solution.num_buses_to_destination(
                routes=case["input"]["routes"],
                source=case["input"]["source"],
                target=case["input"]["target"],
            )
            == case["output"]
        )
