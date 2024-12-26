import pytest
from solutions.sol_494 import Solution


cases = [
    {
        "input": {
            "nums": [1, 1, 1, 1, 1], "target": 3
        },
        "output": 5,
    },
    {
        "input": {
            "nums": [1], "target": 1
        },
        "output": 1,
    },
]


@pytest.mark.sol494
def test_run():
    for case in cases:
        assert (
            Solution.find_target_sum_ways(
                nums=case["input"]["nums"],
                target=case["input"]["target"],
            )
            == case["output"]
        )
