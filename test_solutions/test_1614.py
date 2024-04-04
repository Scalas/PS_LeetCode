import pytest
from solutions.sol_1614 import Solution

cases = [
    {
        "input": {
            "s": "(1+(2*3)+((8)/4))+1",
        },
        "output": 3,
    },
    {
        "input": {
            "s": "(1)+((2))+(((3)))",
        },
        "output": 3,
    },
]


@pytest.mark.sol1614
def test_run():
    for case in cases:
        assert Solution.max_depth(s=case["input"]["s"]) == case["output"]
