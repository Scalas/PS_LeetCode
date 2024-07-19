import pytest
from solutions.sol_1380 import Solution


cases = [
    {
        "input": {"matrix": [[3, 7, 8], [9, 11, 13], [15, 16, 17]]},
        "output": [15],
    },
    {
        "input": {"matrix": [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]},
        "output": [12],
    },
    {
        "input": {"matrix": [[7, 8], [1, 2]]},
        "output": [7],
    },
]


@pytest.mark.sol1380
def test_run():
    for case in cases:
        assert (
            Solution.lucky_numbers(
                matrix=case["input"]["matrix"],
            )
            == case["output"]
        )
