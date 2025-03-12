import pytest
from solutions.sol_2529 import Solution


cases = [
    {
        "input": {"nums": [-2, -1, -1, 1, 2, 3]},
        "output": 3,
    },
    {
        "input": {"nums": [-3, -2, -1, 0, 0, 1, 2]},
        "output": 3,
    },
    {
        "input": {"nums": [5, 20, 66, 1314]},
        "output": 4,
    },
]


@pytest.mark.sol2529
def test_run():
    for case in cases:
        assert (
            Solution.maximum_count(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
