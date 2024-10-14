import pytest
from solutions.sol_1942 import Solution


cases = [
    {
        "input": {"times": [[1, 4], [2, 3], [4, 6]], "targetFriend": 1},
        "output": 1,
    },
    {
        "input": {"times": [[3, 10], [1, 5], [2, 6]], "targetFriend": 0},
        "output": 2,
    },
]


@pytest.mark.sol1942
def test_run():
    for case in cases:
        assert (
            Solution.smallest_chair(
                times=case["input"]["times"],
                targetFriend=case["input"]["targetFriend"],
            )
            == case["output"]
        )
