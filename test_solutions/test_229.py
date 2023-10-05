import pytest
from solutions.sol_229 import Solution

cases = [
    {
        "input": {
            "nums": [3, 2, 3],
        },
        "output": [3],
    },
    {"input": {"nums": [1]}, "output": [1]},
    {"input": {"nums": [1, 2]}, "output": [1, 2]},
]


@pytest.mark.sol229
def test_run():
    for case in cases:
        assert Solution.majority_element(nums=case["input"]["nums"]) == case["output"]
