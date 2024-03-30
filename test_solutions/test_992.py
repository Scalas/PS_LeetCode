import pytest
from solutions.sol_992 import Solution

cases = [
    {
        "input": {
            "nums": [1, 2, 1, 2, 3],
            "k": 2,
        },
        "output": 7,
    },
    {
        "input": {
            "nums": [1, 2, 1, 3, 4],
            "k": 3,
        },
        "output": 3,
    },
]


@pytest.mark.sol992
def test_run():
    for case in cases:
        assert (
            Solution.sub_arrays_with_k_distinct(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
