import pytest
from solutions.sol_442 import Solution

cases = [
    {"input": {"nums": [4, 3, 2, 7, 8, 2, 3, 1]}, "output": [2, 3]},
    {"input": {"nums": [1, 1, 2]}, "output": [1]},
    {"input": {"nums": [1]}, "output": []},
]


@pytest.mark.sol_442
def test_run():
    for case in cases:
        assert (
            Solution.find_duplicates(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
