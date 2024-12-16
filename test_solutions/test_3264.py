import pytest
from solutions.sol_3264 import Solution


cases = [
    {
        "input": {"nums": [2, 1, 3, 5, 6], "k": 5, "multiplier": 2},
        "output": [8, 4, 6, 5, 6],
    },
    {
        "input": {"nums": [1, 2], "k": 3, "multiplier": 4},
        "output": [16, 8],
    },
]


@pytest.mark.sol3264
def test_run():
    for case in cases:
        assert (
            Solution.get_final_state(
                k=case["input"]["k"],
                nums=case["input"]["nums"],
                multiplier=case["input"]["multiplier"],
            )
            == case["output"]
        )
