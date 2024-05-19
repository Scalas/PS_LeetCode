import pytest
from solutions.sol_3068 import Solution

cases = [
    # {
    #     "input": {"nums": [1, 2, 1], "k": 3,  "edges": [[0,1],[0,2]]},
    #     "output": 6,
    # },
    # {
    #     "input": {"nums": [2, 3], "k": 7,  "edges": [[0,1]]},
    #     "output": 9,
    # },
    # {
    #     "input": {"nums": [7,7,7,7,7,7], "k": 3,  "edges": [[0,1],[0,2],[0,3],[0,4],[0,5]]},
    #     "output": 42,
    # },
    # {
    #     "input": {"nums": [1, 1, 1, 1, 1], "k": 3,  "edges": [[0,1],[0,2],[0,3],[0,4]]},
    #     "output": 9,
    # },
    {
        "input": {
            "nums": [24, 78, 1, 97, 44],
            "k": 6,
            "edges": [[0, 2], [1, 2], [4, 2], [3, 4]],
        },
        "output": 260,
    },
]


@pytest.mark.sol_3068
def test_run():
    for case in cases:
        assert (
            Solution.maximumValueSum(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
                edges=case["input"]["edges"],
            )
            == case["output"]
        )
