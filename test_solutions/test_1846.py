import pytest
from solutions.sol_1846 import Solution

cases = [
    {
        "input": {
            "arr": [2, 2, 1, 2, 1],
        },
        "output": 2,
    },
    {
        "input": {
            "arr": [100, 1, 1000],
        },
        "output": 3,
    },
    {
        "input": {
            "arr": [1, 2, 3, 4, 5],
        },
        "output": 5,
    },
]


@pytest.mark.sol1846
def test_run():
    for case in cases:
        assert (
            Solution.maximum_element_after_decrementing_and_rearranging(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
