import pytest
from solutions.sol_624 import Solution


cases = [
    {
        "input": {"arrays": [[1, 2, 3], [4, 5], [1, 2, 3]]},
        "output": 4,
    },
    {
        "input": {"arrays": [[1], [1]]},
        "output": 0,
    },
]


@pytest.mark.sol624
def test_run():
    for case in cases:
        assert (
            Solution.max_distance(
                arrays=case["input"]["arrays"],
            )
            == case["output"]
        )
