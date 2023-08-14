import pytest
from solutions.sol_443 import Solution

cases = [
    {
        "input": {
            "chars": ["a", "a", "b", "b", "c", "c", "c"],
        },
        "output": ["a", "2", "b", "2", "c", "3"],
    },
    {
        "input": {
            "chars": ["a"],
        },
        "output": ["a"],
    },
    {
        "input": {
            "chars": ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
        },
        "output": ["a", "b", "1", "2"],
    },
]


@pytest.mark.sol_443
def test_run():
    for case in cases:
        length = Solution.compress(
            chars=case["input"]["chars"],
        )
        assert case["input"]["chars"][:length] == case["output"]
