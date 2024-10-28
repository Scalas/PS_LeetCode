import pytest
from solutions.sol_2501 import Solution


cases = [
    {
        "input": {"nums": [4, 3, 6, 16, 8, 2]},
        "output": 3,
    },
    {
        "input": {"nums": [2, 3, 5, 6, 7]},
        "output": -1,
    },
]


@pytest.mark.sol2501
def test_run():
    for case in cases:
        assert (
            Solution.longest_square_streak(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
