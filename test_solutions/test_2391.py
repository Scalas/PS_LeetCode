import pytest
from solutions.sol_2391 import Solution

cases = [
    {
        "input": {
            "garbage": ["G", "P", "GP", "GG"],
            "travel": [2, 4, 3],
        },
        "output": 21,
    }
]


@pytest.mark.sol_2391
def test_run():
    for case in cases:
        assert (
            Solution.garbage_collection(
                garbage=case["input"]["garbage"],
                travel=case["input"]["travel"],
            )
            == case["output"]
        )
