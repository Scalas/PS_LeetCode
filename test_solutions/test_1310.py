import pytest
from solutions.sol_1310 import Solution


cases = [
    {
        "input": {"arr": [1, 3, 4, 8], "queries": [[0, 1], [1, 2], [0, 3], [3, 3]]},
        "output": [2, 7, 14, 8],
    },
    {
        "input": {"arr": [4, 8, 2, 10], "queries": [[2, 3], [1, 3], [0, 0], [0, 3]]},
        "output": [8, 0, 4, 4],
    },
]


@pytest.mark.sol1310
def test_run():
    for case in cases:
        assert (
            Solution.xor_queries(
                queries=case["input"]["queries"],
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
