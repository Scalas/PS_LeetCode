import pytest
from solutions.sol_207 import Solution

cases = [
    {
        "input": {
            "num_courses": 2,
            "prerequisites": [[1, 0]],
        },
        "output": True,
    },
    {
        "input": {
            "num_courses": 2,
            "prerequisites": [[1, 0], [0, 1]],
        },
        "output": False,
    },
]


@pytest.mark.sol207
def test_run():
    for case in cases:
        print(case)
        assert (
            Solution.can_finish(
                num_courses=case["input"]["num_courses"],
                prerequisites=case["input"]["prerequisites"],
            )
            == case["output"]
        )
