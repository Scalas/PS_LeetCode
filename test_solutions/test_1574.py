import pytest
from solutions.sol_1574 import Solution


cases = [
    {
        "input": {"arr": [1, 2, 3, 10, 4, 2, 3, 5]},
        "output": 3,
    },
    {
        "input": {"arr": [5, 4, 3, 2, 1]},
        "output": 4,
    },
    {
        "input": {"arr": [1, 2, 3]},
        "output": 0,
    },
]


@pytest.mark.sol1574
def test_run():
    for case in cases:
        assert (
            Solution.find_length_of_shortest_subarray(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
