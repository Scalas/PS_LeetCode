import pytest
from solutions.sol_1791 import Solution


cases = [
    {
        "input": {"edges": [[1, 2], [2, 3], [4, 2]]},
        "output": 2,
    },
    {
        "input": {"edges": [[1, 2], [5, 1], [1, 3], [1, 4]]},
        "output": 1,
    },
]


@pytest.mark.sol1791
def test_run():
    for case in cases:
        assert (
            Solution.find_center(
                edges=case["input"]["edges"],
            )
            == case["output"]
        )
