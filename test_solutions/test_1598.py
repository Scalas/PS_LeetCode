import pytest
from solutions.sol_1598 import Solution


cases = [
    {
        "input": {"logs": ["d1/", "d2/", "../", "d21/", "./"]},
        "output": 2,
    },
    {
        "input": {"logs": ["d1/", "d2/", "./", "d3/", "../", "d31/"]},
        "output": 3,
    },
    {
        "input": {"logs": ["d1/", "../", "../", "../"]},
        "output": 0,
    },
]


@pytest.mark.sol1598
def test_run():
    for case in cases:
        assert (
            Solution.min_operations(
                logs=case["input"]["logs"],
            )
            == case["output"]
        )
