import pytest
from solutions.sol_2045 import Solution


cases = [
    {
        "input": {
            "n": 5, "edges": [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], "time": 3, "change": 5
        },
        "output": 13,
    },
    {
        "input": {
            "n": 2, "edges": [[1, 2]], "time": 3, "change": 2
        },
        "output": 11,
    },
]


@pytest.mark.sol2045
def test_run():
    for case in cases:
        assert (
            Solution.second_minimum(
                time=case["input"]["time"],
                n=case["input"]["n"],
                edges=case["input"]["edges"],
                change=case["input"]["change"],
            )
            == case["output"]
        )
