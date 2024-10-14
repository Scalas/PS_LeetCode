import pytest
from solutions.sol_2406 import Solution


cases = [
    {
        "input": {"intervals": [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]},
        "output": 3,
    },
    {
        "input": {"intervals": [[1, 3], [5, 6], [8, 10], [11, 13]]},
        "output": 1,
    },
]


@pytest.mark.sol2406
def test_run():
    for case in cases:
        assert (
            Solution.min_groups(
                intervals=case["input"]["intervals"],
            )
            == case["output"]
        )
