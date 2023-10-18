import pytest
from solutions.sol_2050 import Solution

cases = [
    {
        "input": {
            "n": 3,
            "relations": [[1, 3], [2, 3]],
            "time": [3, 2, 5],
        },
        "output": 8,
    },
    {
        "input": {
            "n": 5,
            "relations": [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]],
            "time": [1, 2, 3, 4, 5],
        },
        "output": 12,
    },
]


@pytest.mark.sol_2050
def test_run():
    for case in cases:
        assert (
                Solution.minimum_time(
                    n=case["input"]["n"],
                    relations=case["input"]["relations"],
                    time=case["input"]["time"],
                )
                == case["output"]
        )
