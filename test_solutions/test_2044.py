import pytest
from solutions.sol_2044 import Solution


cases = [
    {
        "input": {"nums": [3, 1]},
        "output": 2,
    },
    {
        "input": {"nums": [2, 2, 2]},
        "output": 7,
    },
    {
        "input": {"nums": [3, 2, 1, 5]},
        "output": 6,
    },
]


@pytest.mark.sol2044
def test_run():
    for case in cases:
        assert (
            Solution.count_max_or_subsets(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
