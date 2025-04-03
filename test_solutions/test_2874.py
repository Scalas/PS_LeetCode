import pytest
from solutions.sol_2874 import Solution


cases = []


@pytest.mark.sol2874
def test_run():
    for case in cases:
        assert Solution.maximum_triplet_value() == case["output"]
