import pytest
from solutions.sol_632 import Solution


cases = [
    {
        "input": {"nums": [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]},
        "output": [20, 24],
    },
    {
        "input": {"nums": [[1, 2, 3], [1, 2, 3], [1, 2, 3]]},
        "output": [1, 1],
    },
]


@pytest.mark.sol632
def test_run():
    for case in cases:
        assert (
            Solution.smallest_range(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
