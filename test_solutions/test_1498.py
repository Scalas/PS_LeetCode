import pytest
from solutions.sol_1498 import Solution

cases = [
    {
        "input": {"nums": [3, 5, 6, 7], "target": 9},
        "output": 4,
    },
    {
        "input": {"nums": [3, 3, 6, 8], "target": 10},
        "output": 6,
    },
    {
        "input": {"nums": [2, 3, 3, 4, 6, 7], "target": 12},
        "output": 61,
    },
    {
        "input": {
            "nums": [
                14,
                4,
                6,
                6,
                20,
                8,
                5,
                6,
                8,
                12,
                6,
                10,
                14,
                9,
                17,
                16,
                9,
                7,
                14,
                11,
                14,
                15,
                13,
                11,
                10,
                18,
                13,
                17,
                17,
                14,
                17,
                7,
                9,
                5,
                10,
                13,
                8,
                5,
                18,
                20,
                7,
                5,
                5,
                15,
                19,
                14,
            ],
            "target": 22,
        },
        "output": 272187084,
    },
]


@pytest.mark.sol1498
def test_run():
    for case in cases:
        assert (
            round(
                Solution.num_subseq(
                    nums=case["input"]["nums"],
                    target=case["input"]["target"],
                ),
                5,
            )
            == case["output"]
        )
