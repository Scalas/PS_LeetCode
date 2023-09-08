import pytest
from solutions.sol_118 import Solution

cases = [
    {
        "input": {
            "num_rows": 5,
        },
        "output": [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
    },
    {
        "input": {
            "num_rows": 1,
        },
        "output": [[1]],
    },
]


@pytest.mark.sol118
def test_run():
    for case in cases:
        assert Solution.generate(num_rows=case["input"]["num_rows"]) == case["output"]
