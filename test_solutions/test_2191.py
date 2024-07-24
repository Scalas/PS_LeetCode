import pytest
from solutions.sol_2191 import Solution


cases = [
    {
        "input": {"mapping": [8, 9, 4, 0, 2, 1, 3, 5, 7, 6], "nums": [991, 338, 38]},
        "output": [338, 38, 991],
    },
    {
        "input": {"mapping": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "nums": [789, 456, 123]},
        "output": [123, 456, 789],
    },
]


@pytest.mark.sol2191
def test_run():
    for case in cases:
        assert (
            Solution.sort_jumbled(
                nums=case["input"]["nums"],
                mapping=case["input"]["mapping"],
            )
            == case["output"]
        )
