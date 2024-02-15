import pytest
from solutions.sol_2149 import Solution

cases = [
    {
        "input": {"nums": [3, 1, -2, -5, 2, -4]},
        "output": [3, -2, 1, -5, 2, -4],
    },
    {
        "input": {"nums": [-1, 1]},
        "output": [1, -1],
    },
]


@pytest.mark.sol_2149
def test_run():
    for case in cases:
        assert (
            Solution.rearrange_array(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
