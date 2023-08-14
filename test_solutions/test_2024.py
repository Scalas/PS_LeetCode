import pytest
from solutions.sol_2024 import Solution

cases = [
    {
        "input": {
            "answer_key": "TTFF",
            "k": 2,
        },
        "output": 4,
    },
    {
        "input": {
            "answer_key": "TFFT",
            "k": 1,
        },
        "output": 3,
    },
    {
        "input": {
            "answer_key": "TTFTTFTT",
            "k": 1,
        },
        "output": 5,
    },
]


@pytest.mark.sol_2024
def test_run():
    for case in cases:
        assert (
            Solution.max_consecutive_answers(
                answer_key=case["input"]["answer_key"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
