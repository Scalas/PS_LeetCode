import pytest
from solutions.sol_2134 import Solution


cases = [
    {
        "input": {"nums": [0, 1, 0, 1, 1, 0, 0]},
        "output": 1,
    },
    {
        "input": {"nums": [0, 1, 1, 1, 0, 0, 1, 1, 0]},
        "output": 2,
    },
    {
        "input": {"nums": [1, 1, 0, 0, 1]},
        "output": 0,
    },
]


@pytest.mark.sol2134
def test_run():
    for case in cases:
        assert (
            Solution.min_swaps(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
