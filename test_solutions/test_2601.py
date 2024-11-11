import pytest
from solutions.sol_2601 import Solution


cases = [
    # {
    #     "input": {
    #         "nums": [4, 9, 6, 10]
    #     },
    #     "output": True,
    # },
    # {
    #     "input": {
    #         "nums": [6, 8, 11, 12]
    #     },
    #     "output": True,
    # },
    {
        "input": {"nums": [5, 8, 3]},
        "output": False,
    },
]


@pytest.mark.sol2601
def test_run():
    for case in cases:
        assert (
            Solution.prime_sub_operation(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
