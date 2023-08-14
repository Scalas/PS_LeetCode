import pytest
from solutions.sol_35 import Solution

cases = [
    {"input": {"nums": [1, 3, 5, 6], "target": 5}, "output": 2},
    {"input": {"nums": [1, 3, 5, 6], "target": 2}, "output": 1},
    {"input": {"nums": [1, 3, 5, 6], "target": 7}, "output": 4},
]


@pytest.mark.sol35
def test_run():
    for case in cases:
        assert (
            Solution.search_insert(
                nums=case["input"]["nums"], target=case["input"]["target"]
            )
            == case["output"]
        )
