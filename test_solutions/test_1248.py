import pytest
from solutions.sol_1248 import Solution


cases = [
    {
        "input": {"nums": [1, 1, 2, 1, 1], "k": 3},
        "output": 2,
    },
    {
        "input": {"nums": [2, 4, 6], "k": 1},
        "output": 0,
    },
    {
        "input": {"nums": [2, 2, 2, 1, 2, 2, 1, 2, 2, 2], "k": 2},
        "output": 1,
    },
]


@pytest.mark.sol1248
def test_run():
    for case in cases:
        assert (
            Solution.number_of_sub_arrays(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"],
        )
