import pytest

from solutions.sol_1376 import Solution

cases = [
    {
        "input": {
            "n": 1,
            "head_id": 0,
            "manager": [-1],
            "inform_time": [0],
        },
        "output": 0,
    },
    {
        "input": {
            "n": 6,
            "head_id": 2,
            "manager": [2, 2, -1, 2, 2, 2],
            "inform_time": [0, 0, 1, 0, 0, 0],
        },
        "output": 1,
    },
    {
        "input": {
            "n": 8,
            "head_id": 0,
            "manager": [-1, 5, 0, 6, 7, 0, 0, 0],
            "inform_time": [89, 0, 0, 0, 0, 523, 241, 519],
        },
        "output": 612,
    },
]


@pytest.mark.sol1376
def test_run():
    for case in cases:
        assert (
            Solution.num_of_minutes(
                n=case["input"]["n"],
                head_id=case["input"]["head_id"],
                manager=case["input"]["manager"],
                inform_time=case["input"]["inform_time"],
            )
            == case["output"]
        )
