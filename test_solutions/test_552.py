import pytest
from solutions.sol_552 import Solution

cases = [
    # {
    #     "input": {
    #         "n": 2,
    #     },
    #     "output": 8,
    # },
    # {
    #     "input": {
    #         "n": 1,
    #     },
    #     "output": 3,
    # },
    {
        "input": {
            "n": 10101,
        },
        "output": 183236316,
    },
]


@pytest.mark.sol_552
def test_run():
    for case in cases:
        assert Solution.checkRecord(n=case["input"]["n"]) == case["output"]
