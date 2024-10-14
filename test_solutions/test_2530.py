import pytest
from solutions.sol_2530 import Solution


cases = [
    {
        "input": {"nums": [10, 10, 10, 10, 10], "k": 5},
        "output": 50,
    },
    {
        "input": {"nums": [1, 10, 3, 3, 3], "k": 3},
        "output": 17,
    },
]


@pytest.mark.sol2530
def test_run():
    for case in cases:
        assert (
            Solution.max_k_elements(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
