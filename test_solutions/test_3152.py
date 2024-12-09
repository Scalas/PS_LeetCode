import pytest
from solutions.sol_3152 import Solution


cases = [
    {
        "input": {"nums": [3, 4, 1, 2, 6], "queries": [[0, 4]]},
        "output": [False],
    },
    {
        "input": {"nums": [4, 3, 1, 6], "queries": [[0, 2], [2, 3]]},
        "output": [False, True],
    },
]


@pytest.mark.sol3152
def test_run():
    for case in cases:
        assert (
            Solution.is_array_special(
                nums=case["input"]["nums"],
                queries=case["input"]["queries"],
            )
            == case["output"]
        )
