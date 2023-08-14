import pytest
from solutions.sol_841 import Solution

cases = [
    {"input": {"rooms": [[1], [2], [3], []]}, "output": True},
]


@pytest.mark.sol841
def test_run():
    for case in cases:
        assert (
            Solution.can_visit_all_rooms(rooms=case["input"]["rooms"]) == case["output"]
        )
