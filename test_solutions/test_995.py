import pytest
from solutions.sol_995 import Solution


cases = [
    {
        "input": {"nums": [0, 1, 0], "k": 1},
        "output": 2,
    },
    {
        "input": {"nums": [1, 1, 0], "k": 2},
        "output": -1,
    },
    {
        "input": {"nums": [0, 0, 0, 1, 0, 1, 1, 0], "k": 3},
        "output": 3,
    },
]


@pytest.mark.sol995
def test_run():
    for case in cases:
        assert (
            Solution.min_k_bit_flips(
                k=case["input"]["k"],
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
