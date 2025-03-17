import pytest
from solutions.sol_2206 import Solution


cases = [
    {
        "input": {"nums": [3, 2, 3, 2, 2, 2]},
        "output": True,
    },
    {
        "input": {"nums": [1, 2, 3, 4]},
        "output": False,
    },
]


@pytest.mark.sol2206
def test_run():
    for case in cases:
        assert (
            Solution.divide_array(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
