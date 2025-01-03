import pytest
from solutions.sol_2270 import Solution


cases = [
    {
        "input": {"nums": [10, 4, -8, 7]},
        "output": 2,
    },
    {
        "input": {"nums": [2, 3, 1, 0]},
        "output": 2,
    },
]


@pytest.mark.sol2270
def test_run():
    for case in cases:
        assert (
            Solution.ways_to_split_array(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
