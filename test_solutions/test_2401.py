import pytest
from solutions.sol_2401 import Solution


cases = [
    {
        "input": {"nums": [1, 3, 8, 48, 10]},
        "output": 3,
    },
    {
        "input": {"nums": [3, 1, 5, 11, 13]},
        "output": 1,
    },
]


@pytest.mark.sol2401
def test_run():
    for case in cases:
        assert (
            Solution.longest_nice_subarray(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
