import pytest
from solutions.sol_689 import Solution


cases = [
    {
        "input": {"nums": [1, 2, 1, 2, 6, 7, 5, 1], "k": 2},
        "output": [0, 3, 5],
    },
    {
        "input": {"nums": [1, 2, 1, 2, 1, 2, 1, 2, 1], "k": 2},
        "output": [0, 2, 4],
    },
]


@pytest.mark.sol689
def test_run():
    for case in cases:
        assert (
            Solution.max_sum_of_three_sub_arrays(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
