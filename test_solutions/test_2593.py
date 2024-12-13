import pytest
from solutions.sol_2593 import Solution


cases = [
    {
        "input": {"nums": [2, 1, 3, 4, 5, 2]},
        "output": 7,
    },
    {
        "input": {"nums": [2, 3, 5, 1, 3, 2]},
        "output": 5,
    },
]


@pytest.mark.sol2593
def test_run():
    for case in cases:
        assert (
            Solution.find_score(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
