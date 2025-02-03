import pytest
from solutions.sol_3105 import Solution


cases = [
    {
        "input": {"nums": [1, 4, 3, 3, 2]},
        "output": 2,
    },
    {
        "input": {"nums": [3, 3, 3, 3]},
        "output": 1,
    },
    {
        "input": {"nums": [3, 2, 1]},
        "output": 3,
    },
]


@pytest.mark.sol3105
def test_run():
    for case in cases:
        assert (
            Solution.longest_monotonic_subarray(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
