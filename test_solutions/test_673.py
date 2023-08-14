import pytest
from solutions.sol_673 import Solution

cases = [
    {
        "input": {
            "nums": [1, 3, 5, 4, 7],
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [2, 2, 2, 2, 2],
        },
        "output": 5,
    },
    {
        "input": {
            "nums": [-100, -99, -98, -97, -96, -96],
        },
        "output": 2,
    },
]


@pytest.mark.sol_673
def test_run():
    for case in cases:
        assert (
            Solution.find_number_of_lis(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
