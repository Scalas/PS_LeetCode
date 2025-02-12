import pytest
from solutions.sol_2342 import Solution


cases = [
    {
        "input": {"nums": [18, 43, 36, 13, 7]},
        "output": 54,
    },
    {
        "input": {"nums": [10, 12, 19, 14]},
        "output": -1,
    },
]


@pytest.mark.sol2342
def test_run():
    for case in cases:
        assert (
            Solution.maximum_sum(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
