import pytest
from solutions.sol_1838 import Solution

cases = [
    {
        "input": {
            "nums": [1, 2, 4],
            "k": 5
        },
        "output": 3,
    },
    {
        "input": {
            "nums": [1, 4, 8, 13],
            "k": 5
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [3, 9, 6],
            "k": 2
        },
        "output": 1,
    },
]


@pytest.mark.sol1838
def test_run():
    for case in cases:
        assert (
                Solution.max_frequency(
                    nums=case["input"]["nums"],
                    k=case["input"]["k"],
                )
                == case["output"]
        )
