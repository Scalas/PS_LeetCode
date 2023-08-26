import pytest
from solutions.sol_646 import Solution

cases = [
    {"input": {"pairs": [[1, 2], [2, 3], [3, 4]]}, "output": 2},
    {"input": {"pairs": [[1, 2], [7, 8], [4, 5]]}, "output": 3},
]


@pytest.mark.sol_646
def test_run():
    for case in cases:
        assert (
            Solution.find_longest_chain(
                pairs=case["input"]["pairs"],
            )
            == case["output"]
        )
