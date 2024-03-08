import pytest
from solutions.sol_3005 import Solution

cases = [
    {
        "input": {"nums": [1, 2, 2, 3, 1, 4]},
        "output": 4,
    },
    {
        "input": {"nums": [1, 2, 3, 4, 5]},
        "output": 5,
    },
]


@pytest.mark.sol_3005
def test_run():
    for case in cases:
        assert (
            Solution.max_frequency_elements(nums=case["input"]["nums"])
            == case["output"]
        )
