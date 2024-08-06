import pytest
from solutions.sol_3016 import Solution


cases = [
    {
        "input": {
            "word": "abcde"
        },
        "output": 5,
    },
    {
        "input": {
            "word": "xyzxyzxyzxyz"
        },
        "output": 12,
    },
    {
        "input": {
            "word": "aabbccddeeffgghhiiiiii"
        },
        "output": 24,
    },
]


@pytest.mark.sol3016
def test_run():
    for case in cases:
        assert (
            Solution.minimum_pushes(
                word=case["input"]["word"],
            )
            == case["output"]
        )
