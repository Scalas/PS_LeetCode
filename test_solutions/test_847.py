import pytest
from solutions.sol_847 import Solution

cases = [
    {"input": {"graph": [[1, 2, 3], [0], [0], [0]]}, "output": 4},
    {"input": {"graph": [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]}, "output": 4},
    {"input": {"graph": [[]]}, "output": 0},
]


@pytest.mark.sol847
def test_run():
    for case in cases:
        assert (
            Solution.shortest_path_length(graph=case["input"]["graph"])
            == case["output"]
        )
