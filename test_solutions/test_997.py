import pytest
from solutions.sol_997 import Solution

cases = [
    {"input": {"n": 2, "trust": [[1, 2]]}, "output": 2},
    {"input": {"n": 3, "trust": [[1, 3], [2, 3]]}, "output": 3},
    {"input": {"n": 3, "trust": [[1, 3], [2, 3], [3, 1]]}, "output": -1},
]


@pytest.mark.sol997
def test_run():
    for case in cases:
        assert (
            Solution.find_judge(n=case["input"]["n"], trust=case["input"]["trust"])
            == case["output"]
        )
