import pytest
from solutions.sol_452 import Solution

cases = [
    {"input": {"points": [[10, 16], [2, 8], [1, 6], [7, 12]]}, "output": 2},
    {"input": {"points": [[1, 2], [3, 4], [5, 6], [7, 8]]}, "output": 4},
    {"input": {"points": [[1, 2], [2, 3], [3, 4], [4, 5]]}, "output": 2},
]


@pytest.mark.sol_452
def test_run():
    for case in cases:
        assert (
            Solution.find_min_arrow_shots(points=case["input"]["points"])
            == case["output"]
        )
