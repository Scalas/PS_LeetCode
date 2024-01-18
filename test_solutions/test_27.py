import pytest
from solutions.sol_27 import Solution

cases = [
    {
        "input": {
            "nums": [3, 2, 2, 3],
            "val": 3,
        },
        "output": [2, [2, 2]],
    },
    {
        "input": {
            "nums": [0, 1, 2, 2, 3, 0, 4, 2],
            "val": 2,
        },
        "output": [5, [0, 1, 3, 0, 4]],
    },
]


@pytest.mark.sol27
def test_run():
    for case in cases:
        res = Solution.remove_element(
            nums=case["input"]["nums"], val=case["input"]["val"]
        )
        assert res == case["output"][0]
        assert case["input"]["nums"][:res] == case["output"][1]
