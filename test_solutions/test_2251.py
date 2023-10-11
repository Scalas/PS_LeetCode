import pytest
from solutions.sol_2251 import Solution

cases = [
    {
        "input": {
            "flowers": [[1, 6], [3, 7], [9, 12], [4, 13]],
            "people": [2, 3, 7, 11],
        },
        "output": [1, 2, 2, 2],
    },
    {"input": {"flowers": [[1, 10], [3, 3]], "people": [3, 3, 2]}, "output": [2, 2, 1]},
]


@pytest.mark.sol_2251
def test_run():
    for case in cases:
        assert (
            Solution.fullBloom_flowers(
                flowers=case["input"]["flowers"], people=case["input"]["people"]
            )
            == case["output"]
        )
