import pytest
from solutions.sol_2762 import Solution


cases = [
    {
        "input": {"nums": [5, 4, 2, 4]},
        "output": 8,
    },
    {
        "input": {"nums": [1, 2, 3]},
        "output": 6,
    },
]


@pytest.mark.sol2762
def test_run():
    for case in cases:
        assert (
            Solution.continuous_sub_arrays(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
