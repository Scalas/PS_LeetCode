import pytest
from solutions.sol_962 import Solution


cases = [
    {
        "input": {"nums": [6, 0, 8, 2, 1, 5]},
        "output": 4,
    },
    {
        "input": {"nums": [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]},
        "output": 7,
    },
]


@pytest.mark.sol962
def test_run():
    for case in cases:
        assert (
            Solution.max_width_ramp(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
